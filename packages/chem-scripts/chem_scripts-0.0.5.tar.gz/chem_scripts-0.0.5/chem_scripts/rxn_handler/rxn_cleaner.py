#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 17:17
# @Author  : zbc@mail.ustc.edu.cn
# @File    : rxn_cleaner.py
# @Software: PyCharm

from typing import Optional

from rdkit.Chem import AllChem
from rdkit.Chem.rdchem import Mol

from chem_scripts.mol_handler import MolSmiles


class RxnCleaner:

    @classmethod
    def _is_mol_mapped(cls, mol: Mol) -> bool:
        for atom in mol.GetAtoms():
            if atom.GetAtomMapNum() != 0:
                return True
        return False

    @classmethod
    def _get_mapped_mols(cls, mols: [Mol]) -> [Mol]:
        new_mols = []
        for mol in mols:
            if cls._is_mol_mapped(mol):
                new_mols.append(mol)
        return new_mols

    @classmethod
    def remove_products_same_with_reactants(cls, rxn: AllChem.ChemicalReaction) -> AllChem.ChemicalReaction:
        reactants_smileses = [MolSmiles.get_smiles_without_map_num(mol) for mol in rxn.GetReactants()]
        new_rxn = AllChem.ChemicalReaction()
        has_product = False
        for product in rxn.GetProducts():
            p_smiles = MolSmiles.get_smiles_without_map_num(product)
            if p_smiles in reactants_smileses:
                continue
            new_rxn.AddProductTemplate(product)
            has_product = True
        if has_product:
            for reactant in rxn.GetReactants():
                new_rxn.AddReactantTemplate(reactant)
        return new_rxn

    @classmethod
    def clean_unmapped(cls, rdrxn: AllChem.ChemicalReaction) -> Optional[AllChem.ChemicalReaction]:
        products = rdrxn.GetProducts()
        reactants = rdrxn.GetReactants()

        mapped_reactants = cls._get_mapped_mols(reactants)
        mapped_products = cls._get_mapped_mols(products)
        if len(mapped_products) == 0 or len(mapped_reactants) == 0:
            return None
        new_rdrxn = AllChem.ChemicalReaction()
        for reactant in mapped_reactants:
            new_rdrxn.AddReactantTemplate(reactant)
        for product in mapped_products:
            new_rdrxn.AddProductTemplate(product)
        return new_rdrxn

    @classmethod
    def is_mappable(cls, rdrxn: AllChem.ChemicalReaction) -> bool:
        products = rdrxn.GetProducts()
        reactants = rdrxn.GetReactants()
        reactants_map_nums = set()
        for reactant in reactants:
            for atom in reactant.GetAtoms():
                reactants_map_nums.add(atom.GetAtomMapNum())
        for product in products:
            for atom in product.GetAtoms():
                map_num = atom.GetAtomMapNum()
                if map_num == 0:
                    return False
                elif map_num not in reactants_map_nums:
                    return False
        return True


if __name__ == "__main__":
    pass
