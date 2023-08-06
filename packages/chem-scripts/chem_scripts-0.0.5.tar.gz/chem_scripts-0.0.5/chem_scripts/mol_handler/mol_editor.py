#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 20:17
# @Author  : zhangbc0315@outlook.com
# @File    : mol_editor.py
# @Software: PyCharm

from rdkit.Chem.rdchem import EditableMol, Mol
from rdkit.Chem import AllChem


class MolEditor:

    @classmethod
    def combine_mols(cls, mols):
        combined_mol = None
        for mol in mols:
            if combined_mol is None:
                combined_mol = mol
            else:
                combined_mol = AllChem.CombineMols(combined_mol, mol)
        return combined_mol

    @classmethod
    def frag_idxes_to_mol(cls, mol, idxes: [int]):
        em = EditableMol(Mol())
        idxes_old_to_new = {}
        for i, idx in enumerate(idxes):
            em.AddAtom(mol.GetAtomWithIdx(idx))
            idxes_old_to_new[idx] = i

        for i, idx in enumerate(idxes):
            atom = mol.GetAtomWithIdx(idx)
            for bond in atom.GetBonds():
                if bond.GetBeginAtomIdx() == idx:
                    other_idx = bond.GetEndAtomIdx()
                else:
                    other_idx = bond.GetBeginAtomIdx()
                if other_idx < idx:
                    continue
                if other_idx in idxes_old_to_new.keys():
                    em.AddBond(idxes_old_to_new[idx], idxes_old_to_new[other_idx], bond.GetBondType())
        res = em.GetMol()
        res.ClearComputedProps()
        AllChem.GetSymmSSSR(res)
        res.UpdatePropertyCache(False)
        res._idxMap = idxes_old_to_new
        return res

    @classmethod
    def canonical_rank_atoms(cls, mol):
        idx_to_old_map = {}
        for idx, atom in enumerate(mol.GetAtoms()):
            idx_to_old_map[idx] = atom.GetAtomMapNum()
            atom.SetAtomMapNum(0)
        atoms_ranks = list(AllChem.CanonicalRankAtoms(mol, breakTies=True))
        ranked_atom_idxes = []
        for r in range(len(atoms_ranks)):
            ranked_atom_idxes.append(atoms_ranks.index(r))
        return ranked_atom_idxes, idx_to_old_map

    @classmethod
    def canonicalize_map_num(cls, mol):
        map_num_old_to_new = {}
        new_map_num = 1
        ranked_atom_idxes, idx_to_old_map = cls.canonical_rank_atoms(mol)
        for idx in ranked_atom_idxes:
            atom = mol.GetAtomWithIdx(idx)
            old_map_num = idx_to_old_map[idx]
            if old_map_num == 0:
                continue
            if old_map_num in map_num_old_to_new.keys():
                atom.SetAtomMapNum(map_num_old_to_new[old_map_num])
            else:
                atom.SetAtomMapNum(new_map_num)
                map_num_old_to_new[old_map_num] = new_map_num
                new_map_num += 1
        AllChem.CanonicalizeMol(mol)
        return map_num_old_to_new


if __name__ == "__main__":
    pass
