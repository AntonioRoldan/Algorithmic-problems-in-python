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

BinTreeNode* find_minimum(BinTreeNode* root){
    while(root->left != NULL){
        root = root->left;
    }
    return root;
    //Once we have traversed it until one or both of the children are null
}

void deletion(BinTreeNode* tree, int key){
    BinTreeNode* node = find_node(tree, key);
    BinTreeNode* parent = node->parent;
    BinTreeNode* minimum;
    int children_count = count_children(node);
    if(tree->right == NULL and tree->left == NULL){
        tree = NULL;
    }
    if(children_count == 0){
        if (parent->right == node){
            parent->right = NULL;
        } else{
            parent->left = NULL;
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
        minimum = find_minimum(node); //We find minimum value in right subtree
        node->value = minimum->value;
        deletion(minimum, minimum->value);
        delete minimum;
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

BinTreeNode* set_tree(){
    BinTreeNode* t = tree_insert(0, 6);
    tree_insert(t, 10);
    tree_insert(t, 5);
    tree_insert(t, 2);
    tree_insert(t, 3);
    tree_insert(t, 4);
    tree_insert(t, 11);
    tree_insert(t, 1);
    tree_insert(t, 9);
    return t;
}

int main(int argc, char *argv[])
{
    BinTreeNode* t = set_tree();
    std::cout<<"Case 1, zero children: "<<std::endl;
    BinTreeNode* case1 = set_tree();
    std::cout<<"Tree before deletion: "<<std::endl;
    in_order(case1);
    deletion(case1, 1);
    std::cout<<"Tree after deletion: "<<std::endl;
    in_order(case1);
    std::cout<<"Case 2, one child: "<<std::endl;
    BinTreeNode* case2 = set_tree();
    std::cout<<"Tree before deletion: "<<std::endl;
    in_order(case2);
    deletion(case2, 3);
    std::cout<<"Tree after deletion: "<<std::endl;
    in_order(case2);
    std::cout<<"Case 3, two children: "<<std::endl;
    BinTreeNode* case3 = set_tree();
    std::cout<<"Tree before deletion: "<<std::endl;
    in_order(case3);
    deletion(case3, 2);
    std::cout<<"Tree after deletion: "<<std::endl;
    in_order(case3);
    return 0;
}
