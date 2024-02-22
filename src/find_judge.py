"""
997. Find the Town Judge
Easy
Topics
Companies
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai
trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""

from typing import List
from icecream import ic


def find_judge(n: int, trust: List[List[int]]) -> int:
    trusts = [0] * n
    trusted = [0] * n
    for person, trust_i in trust:
        trusted[trust_i - 1] += 1
        trusts[person - 1] += 1
    ic(trust, trusts, trusted)
    for i, (n_trusts, n_trusted) in enumerate(zip(trusts, trusted)):
        if n_trusts == 0 and n_trusted == n - 1:
            return i + 1
    return -1


if __name__ == '__main__':
    find_judge(n=3, trust=[[1, 2], [2, 3]])
