#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 15:08
# @Author  : zhangbc0315@outlook.com
# @File    : rxn_template_extractor.py
# @Software: PyCharm

from enum import Enum
import logging

from chem_scripts.rxn_template_handler.rxn_center_detector import RxnCenterDetector
from chem_scripts.mol_handler import MolEditor
from chem_scripts.rxn_handler import RxnCleaner

from rdkit.Chem import AllChem


class RtType(Enum):

    CENTRAL_WITHOUT_H = 0
    CENTRAL_WITH_H = 1
    EXTEND_WITHOUT_H = 2
    EXTEND_WITH_H = 3


class RxnTemplateExtractor:

    @classmethod
    def _unique_map_num(cls, mols) -> bool:
        map_nums = set()
        for mol in mols:
            for atom in mol.GetAtoms():
                map_num = atom.GetAtomMapNum()
                if map_num == 0:
                    continue
                if map_num in map_nums:
                    return False
                map_nums.add(map_num)
        return True

    @classmethod
    def _get_rxn_template(cls, reactants, product, reactant_atom_idxes_list, product_atom_idxes):
        rxn_template = AllChem.ChemicalReaction()
        for reactant, r_atom_idxes in zip(reactants, reactant_atom_idxes_list):
            if len(r_atom_idxes) == 0:
                continue
            r_frag = MolEditor.frag_idxes_to_mol(reactant, r_atom_idxes)
            rxn_template.AddReactantTemplate(r_frag)
        p_frag = MolEditor.frag_idxes_to_mol(product, product_atom_idxes)
        rxn_template.AddProductTemplate(p_frag)
        return rxn_template

    @classmethod
    def canon_rxn_template(cls, rxn_template: AllChem.ChemicalReaction):
        map_num_old_to_new = MolEditor.canonicalize_map_num(rxn_template.GetProducts()[0])
        for atom in rxn_template.GetReactants()[0].GetAtoms():
            map_num = atom.GetAtomMapNum()
            if map_num != 0:
                atom.SetAtomMapNum(map_num_old_to_new[map_num])
        AllChem.CanonicalizeMol(rxn_template.GetReactants()[0])

    @classmethod
    def _remove_hs(cls, rxn):
        for r in rxn.GetReactants():
            for atom in r.GetAtoms():
                atom.SetNumExplicitHs(0)
        for p in rxn.GetProducts():
            for atom in p.GetAtoms():
                atom.SetNumExplicitHs(0)

    @classmethod
    def rxn_smiles_to_rt_smarts(cls, rxn_smiles: str, rt_type: RtType = RtType.CENTRAL_WITHOUT_H):
        rxn = AllChem.ReactionFromSmarts(rxn_smiles, useSmiles=True)
        if rxn.GetNumProductTemplates() != 1:
            logging.warning(f"Expect 1 product, but get {rxn.GetNumProducts()}")
            return None
        if rxn.GetNumReactantTemplates() < 1:
            logging.warning(f"Expect at least 1 reactants, but get {rxn.GetNumReactants()}")
            return None

        rxn = RxnCleaner.remove_products_same_with_reactants(rxn)
        if not RxnCleaner.is_mappable(rxn):
            logging.warning(f"wrong rxn smiles: {rxn_smiles}")
            return None

        reactants = list(rxn.GetReactants())
        reactants = [MolEditor.combine_mols(reactants)]
        product = rxn.GetProducts()[0]
        if not (cls._unique_map_num(reactants) and cls._unique_map_num([product])):
            logging.warning(f"Duplicated map number is existed in reaction: {rxn_smiles}")
            return None
        reactants_atom_idxes_list, product_atom_idxes = RxnCenterDetector.get_center_atom_idxes(reactants, product)
        if all([len(rs) == 0 for rs in reactants_atom_idxes_list]):
            logging.warning(f"Number of reaction center in reactants is 0, rxn smiles: {rxn_smiles}")
            return None
        if len(product_atom_idxes) == 0:
            logging.warning(f"Number of reaction center in product is 0, rxn smiles: {rxn_smiles}")
            return None
        rxn_template = cls._get_rxn_template(reactants, product, reactants_atom_idxes_list, product_atom_idxes)
        if rt_type in [RtType.CENTRAL_WITHOUT_H, RtType.EXTEND_WITHOUT_H]:
            cls._remove_hs(rxn_template)
        cls.canon_rxn_template(rxn_template)
        return AllChem.ReactionToSmiles(rxn_template, canonical=True)


if __name__ == "__main__":
    smi = '[C:1]([CH3:2])([CH3:3])([CH3:4])[c:5]1[cH:6][cH:7][c:8]([OH:11])[cH:9][cH:10]1>>[C:1]([CH3:2])([CH3:3])([CH3:4])[CH:5]1[CH2:6][CH2:7][CH:8]([OH:11])[CH2:9][CH2:10]1'
    print(RxnTemplateExtractor.rxn_smiles_to_rt_smarts(smi))
