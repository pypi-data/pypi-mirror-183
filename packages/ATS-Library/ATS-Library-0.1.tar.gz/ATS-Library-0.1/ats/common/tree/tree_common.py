from treelib import Tree

TAG = "TreeCommon"


class TreeCommon(object):

    @staticmethod
    def get_tree_root():
        """
        获取树根
        :return: 树根
        """
        return Tree()

    @staticmethod
    def create_tree(tree_list):
        """
        创建树结构
        :param tree_list: 树列表
        :return: 树结构
        """
        tree = Tree()
        for node in tree_list:
            tree.create_node(*node)
        return tree

    @staticmethod
    def get_node_path_by_id(tree, node_id):
        """
        获取节点路径
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点路径
        """
        path = []
        node_tree = tree.rsearch(node_id)
        while True:
            try:
                path.append(next(node_tree))
            except StopIteration as e:
                break
        return path

    @staticmethod
    def get_node_path_by_tag(tree, node_id):
        """
        获取节点路径
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点路径
        """
        path = []
        node_tree = tree.rsearch(node_id)
        while True:
            try:
                nodes_id = next(node_tree)
                tag_name = TreeCommon.translate_node_id2tag(tree, nodes_id)
                path.append(tag_name)
            except StopIteration as e:
                break
        return path

    @staticmethod
    def translate_node_id2tag(tree, node_id):
        """
        节点id转换为tag
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点tag
        """
        node = tree.get_node(node_id)
        tag = node.tag
        return tag

    @staticmethod
    def show_tree(tree):
        """
        展示树结构
        :param tree: 树结构
        :return: None
        """
        tree.show()

    @staticmethod
    def get_tree_node(tree, node_id):
        """
        获取树节点
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点
        """
        return tree.get_node(node_id)

    @staticmethod
    def get_tree_node_children(tree, node_id):
        """
        获取树节点的子节点
        :param tree: 树结构
        :param node_id: 节点id
        :return: 子节点
        """
        return tree.children(node_id)

    @staticmethod
    def get_tree_node_father(tree, node_id):
        """
        获取树节点的父节点
        :param tree: 树结构
        :param node_id: 节点id
        :return: 父节点
        """
        return tree.parent(node_id)

    @staticmethod
    def get_tree_node_siblings(tree, node_id):
        """
        获取树节点的兄弟节点
        :param tree: 树结构
        :param node_id: 节点id
        :return: 兄弟节点
        """
        return tree.siblings(node_id)

    @staticmethod
    def get_tree_node_depth(tree, node_id):
        """
        获取树节点的深度
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点深度
        """
        return tree.depth(node_id)

    @staticmethod
    def get_tree_node_height(tree, node_id):
        """
        获取树节点的高度
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点高度
        """
        return tree.height(node_id)

    @staticmethod
    def get_tree_node_size(tree, node_id):
        """
        获取树节点的大小
        :param tree: 树结构
        :param node_id: 节点id
        :return: 节点大小
        """
        return tree.size(node_id)
