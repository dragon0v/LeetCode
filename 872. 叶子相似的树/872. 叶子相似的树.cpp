// 解题思路
// 用一个数组保存root1的中序遍历结果，
// 再让该数组与root2中序遍历比较

// 代码


 // Definition for a binary tree node.
 struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 };

int size;
int count;
void inorder(int* arr,struct TreeNode* root)
{
    if(root)
    {
        inorder(arr,root->left);
        if(!root->left&&!root->right)//必须是叶子节点
            arr[size++]=root->val;
        inorder(arr,root->right);
    }
}
void check(int* arr,struct TreeNode* root)
{
    if(root)
    {
        check(arr,root->left);
        if(!root->left&&!root->right)
            if(root->val==arr[count])//相等则计数器+1
                count++;
            else
                count=0;//否则置0，则count与size不可能相等
        check(arr,root->right);
    }
}


bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    if(root1==NULL&&root2==NULL)
        return true;
    if(root1==NULL||root2==NULL)
        return false;
    size=count=0;
    int arr[201]={0};
    inorder(arr,root1);//遍历root1把结果保存在arr中
    check(arr,root2);//检查root2是否有与root1一样的叶子序列
    return count==size;//如果count=size，说明相等
}

// 作者：mrggls-t
// 链接：https://leetcode-cn.com/problems/leaf-similar-trees/solution/zhi-yong-yi-ge-shu-zu-jie-jue-shi-jian-ji-bai-bai-/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。