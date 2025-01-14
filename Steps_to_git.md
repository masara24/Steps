
## Git command

- config

```

git config --global user.email "Clear@Clear.com"

git config --global user.name "Clear"

git config --global -l



```

- clone or pull

```
git clone https://github.com/masara24/Steps.git

# https only, disable ssl
git config --global http.sslVerify false

# pull force the local 
git fetch --all
git reset --hard origin/main
git pull
```

- add remote and push

```
git remote add origin https://github.com/masara24/Steps.git

# the nextline...
git config core.autocrlf false

git add *
git commit -m "update"
git push

# use token
git remote set-url origin https://<your_token>@github.com/masara24/Steps.git
```

## Windows Log

```
C:\Users\Administrator\Downloads\PortableGit>chcp 437
Active code page: 437

C:\Users\Administrator\Downloads\PortableGit>git config --global -l

C:\Users\Administrator\Downloads\PortableGit>git config --global http.proxy 127.0.0.1:1080

C:\Users\Administrator\Downloads\PortableGit>git config --global https.proxy 127.0.0.1:1080

C:\Users\Administrator\Downloads\PortableGit>git config --global --unset http.proxy

C:\Users\Administrator\Downloads\PortableGit>git config --global --unset https.proxy

C:\Users\Administrator\Downloads\PortableGit>dir
 Volume in drive C is 22H2
 Volume Serial Number is F492-73AD

 Directory of C:\Users\Administrator\Downloads\PortableGit

2024-12-25  13:45    <DIR>          .
2024-12-25  13:45    <DIR>          ..
2024-12-25  13:19    <DIR>          bin
2024-12-25  13:19    <DIR>          cmd
2024-12-25  13:19    <DIR>          dev
2024-12-25  13:19    <DIR>          etc
2024-11-25  20:16           139,144 git-bash.exe
2024-11-25  20:16           138,616 git-cmd.exe
2024-11-25  20:28            18,765 LICENSE.txt
2024-12-25  13:19    <DIR>          mingw64
2024-12-25  13:22    <DIR>          python310
2024-11-25  20:27             3,738 README.portable
2024-11-25  20:28    <DIR>          tmp
2024-12-25  13:19    <DIR>          usr
               4 File(s)        300,263 bytes
              10 Dir(s)  72,453,459,968 bytes free

C:\Users\Administrator\Downloads>git clone https://github.com/masara24/Steps.git
Cloning into 'Steps'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (4/4), done.

C:\Users\Administrator\Downloads>cd Steps

C:\Users\Administrator\Downloads\Steps>dir
 Volume in drive C is 22H2
 Volume Serial Number is F492-73AD

 Directory of C:\Users\Administrator\Downloads\Steps

2024-12-25  13:56    <DIR>          .
2024-12-25  13:56    <DIR>          ..
2024-12-25  13:56             1,086 LICENSE
2024-12-25  13:56                 7 README.md
               2 File(s)          1,093 bytes
               2 Dir(s)  72,452,886,528 bytes free

C:\Users\Administrator\Downloads\Steps>
```

