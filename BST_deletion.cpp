#include <iostream>

class BinTreeNode {
public:
    BinTreeNode(int value, BinTreeNode* parent) {
        this->value = value;
        this->left = NULL;
        this->right = NULL;
        this->parent = parent;
    }
    int value;
    BinTreeNode* left;
    BinTreeNode* right;
    BinTreeNode* parent;

};

BinTreeNode* tree_insert(BinTreeNode* tree, int item) {
    if (tree == NULL)
        tree = new BinTreeNode(item, NULL);
    else
    if (item < tree->value)
        if (tree->left == NULL)
            tree->left = new BinTreeNode(item, tree);
        else
            tree_insert(tree->left, item);
    else if (tree->right == NULL)
        tree->right = new BinTreeNode(item, tree);
    else
        tree_insert(tree->right, item);
    return tree;
}

int count_children(BinTreeNode* tree){
    int count = 0;
    if (tree->left){
        count += 1;
    }
    if(tree->right){
        count += 1;
    }
    return count;
}

BinTreeNode* find_node(BinTreeNode* tree, int key){
    if (tree->value == key or tree == 0){
        return tree;
    } else if (tree->value > key){
            return find_node(tree->left, key);
    } else if (tree->value < key){
        return find_node(tree->right, key);
    }
    return 0;
}

BinTreeNode* get_parent(BinTreeNode* tree){
    return tree->parent;
}

void deletion(BinTreeNode* tree, int key){
    BinTreeNode* node = find_node(tree, key);
    BinTreeNode* parent = node->parent;
    BinTreeNode* temp;
    int children_count = count_children(node);
    int p_value = parent->value;
    if(children_count == 0){
        if (parent->right == node){
            parent->right = NULL;
        } else{
            parent->left == NULL;
        }
        parent->left = NULL;
    } else if(children_count == 1){
        if (node->left == NULL){
            node = node->right;
            parent->right = node;
            node->right = NULL;
        } else{
            node = node->left;
            parent->left = node;
            node->left = NULL;
        }
    } else{
        
    }
}

void postorder(BinTreeNode* tree) {
    if (tree->left != NULL)
        postorder(tree->left);
    if (tree->right != NULL)
        postorder(tree->right);
    std::cout << tree->value << std::endl;

}

void in_order(BinTreeNode* tree) {
    if (tree->left != NULL)
        in_order(tree->left);
    std::cout << tree->value << std::endl;
    if (tree->right != NULL)
        in_order(tree->right);
}

int main(int argc, char *argv[])
{
    BinTreeNode* t = tree_insert(0, 6);
    tree_insert(t, 10);
    tree_insert(t, 5);
    tree_insert(t, 2);
    tree_insert(t, 3);
    tree_insert(t, 4);
    tree_insert(t, 11);
    tree_insert(t, 1);
    in_order(t);
    std::cout<<find_node(t, 2)<<std::endl;
    deletion(t, 1);
    in_order(t);
    return 0;
}
