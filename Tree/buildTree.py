from typing import List

# 전위, 중위 순회의 결과로 이진 트리 복원

# implement TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        # preorder의 첫 번째 원소를 pop하여 inorder에서의 index를 찾는다.
        # 전위 순회의 첫 번째 원소는 항상 루트 노드이므로, 이를 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 나눌 수 있다.
        # 따라서 중위 순회의 분할정복 문제로 볼 수 있다.
        index = inorder.index(preorder.pop(0))

    node = TreeNode(inorder[index])
    node.left = build_tree(preorder, inorder[0:index])
    node.right = build_tree(preorder, inorder[index + 1:])

    return node
