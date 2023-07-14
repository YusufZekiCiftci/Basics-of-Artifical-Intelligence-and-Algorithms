

tree= [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
root=0
prun=0

def childs(branch,depth,alpha,beta):
    global tree
    global root
    global prun
    i=0
    
    for child in branch:
        if type(child) is list:
            (n_alpha,n_beta)=childs(child, depth+1, alpha, beta)
            if depth%2==1:
                beta=n_alpha if n_alpha<beta else beta
            else:
                alpha=n_beta if n_beta>alpha else alpha
                branch[i]=alpha if depth%2==0 else beta
                i+=1
        else:
            if depth%2==0 and alpha<child:
                alpha=child
            if depth%2==1 and beta>child:
                beta=child
            if alpha>=beta:
                prun+=1
                break
    if depth==root:
        tree=alpha if root==0 else beta
        return (alpha,beta)
    #%%
def abp(in_tree=tree,begin=root,bott=-15,top=15):
    global tree
    global prun
    global root
    (alpha,beta)=childs(tree, begin, bott, top)
    if __name__=="__main__":
        print("(alpha, beta): ",alpha,beta)
        print("Result: ",tree)
        print("Num of Prun: ",prun)
    return (alpha,beta,prun,tree)
if __name__=="__main__":
    abp(None)
            