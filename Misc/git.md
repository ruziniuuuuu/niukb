# git

## 记录在GitHub上隐藏敏感信息

起因是我把某个带有敏感信息的文件上传到GitHub了，并且因此收到了GitHub的“Generic High Entropy Secret exposed on GitHub”的提示邮件（之前是private库所以一直没有提示，转public之后才收到的邮件），因此我的想法是在该repo的整个历史中抹掉这条敏感信息的存在，最开始是想着用`git filter-branch`的。具体流程如下：

```bash
#!/bin/bash

# 替换敏感信息
git filter-branch --tree-filter '
    if [ -f path/to/your/file ]; then
        sed -i "s/sensitive_info/replaced_info/g" path/to/your/file
    fi
' --prune-empty --tag-name-filter cat -- --all

# 强制推送到远程仓库
git push origin --force --all

# 清理和回收空间
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now
```

但最终再三思考还是没有选择用`git filter-branch`，因为发现用`git rebase -i`似乎是更现代且更方便的一种方式。

1. 通过交互式变基来修改或删除包含敏感信息的提交
   1. `git rebase -i HEAD~n`
   2. 在编辑器里把想要修改的commit前的`pick`改为`edit`
   3. `git commit --amend --no-edit`：使用修改后的文件更新提交，同时保持提交信息不变
   4. `git rebase --continue`直到所有标记为`edit`的提交都被处理
2. 修改后强制推送新的历史(`git push --force`)

另外还有一个问题是，我需要在另一台电脑（服务器）上更新这个更改，由于commit历史在GitHub被更改了，然后服务器本地并没有变更，所以如果直接`git pull`的话会爆错(`Automatic merge failed; fix conflicts and then commit the result.`)。

对于该种情况我的处理流程如下：

1. `git fetch --all`：更新远程引用，但不合并更改
2. `git reset --hard origin/main`：重置本地分支到远程分支的状态
