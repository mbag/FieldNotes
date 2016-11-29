Setting Git server on Linux machine
===================================

1. Create user git user using standard useradd command	
2. initiate bare repository `git init --bare test.git`
3. After initialization do the following 
```
mv hooks/post-update.sample hooks/post-update
$ chmod a+x hooks/post-update
```
4. run `git update-server-info`

More on configuration for various git protocols https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols
