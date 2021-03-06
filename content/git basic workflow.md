Title: Git basic workflow
Date: 2019-02-08 10:20
Modified: 2019-02-16 18:30
Category: Misc
Tags: git
Slug: git basic workflow
Authors: Gonzalo Saenz
Status: published
Summary: This post describes a basic git workflow. This is what I follow to keep track of changes in this blog.

This post describes a basic git workflow. This is what I follow to keep track of changes in this blog.

I will cover, how to create a [bare repository](#bare), a [local repository](#local), and the [workflow](#workflow) to make changes.

All examples will be based on a [Pelican][] blog, but you can follow the same principles for any type of git repository.

# Bare Repository <a name="bare"></a>

The bare repository is a non working repository. It's impossible to edit files and commit changes in it. The whole idea of a bare repository is to pull and push into it, but never directly commit into it. A bare repository is just used for storage, as opposed to a development repository.

![git_repository][]

```shell
git init --bare gonzalosaenz.com.git
```

# Local repository <a name="local"></a>

A local repository can be created with

```shell
git init gonzalosaenz.com
```

This will create an empty local repository. You can create and edit files in the local repository with your favorite text editor. Once you create files, they can be added your git repository within

```shell
git add .
```

Once you finish working on your files. you can perform a:

```shell
git status
```
This will list any pending changes. Then you might:

```shell
git add . # too add any pending changes
git commit -m "commit message."
```

This will commit your changes to your local repository. However we haven't linked yet the local and remote (bare) repositories. in order to do so,

```shell
git remote add gonzalosaenz.com me@gitserver.com:~/gonzalosaenz.com.git
git push --set-upstream gonzalosaenz.com master
```
In case it needs to be clarified, "me@gitserver.com:~/gonzalosaenz.com.git" is a fake repository. You can use [github][], [gitlab][], [bitbucket][], hosted a repository in your own (cloud) server, etc.

Next step is to push your local copy of the repository to the remote repository. This will make your local changes available in the remote repository.

```shell
git push gonzalosaenz.com
```

In the local repository you can query your remote repository with:

```shell
git remote -v
origin  me@gitserver.com:~/gonzalosaenz.com.git (fetch)
origin  me@gitserver.com:~/gonzalosaenz.com.git (push)
```

# Workflow <a name="workflow"></a>

So far we covered the steps that are required to create a bare repository and a local working repository. You only need to perform these steps once.

Now we will cover the git workflow to work on your content. The steps I follow every time I write a new post, I would:

1) clone a local copy of the repository:

```shell
git clone me@gitserver.com:~/gonzalosaenz.com.git
cd gonzalosaenz.com
```

2) Create my working environment

```shell
virtualenv . # create a virtualenv for Pelican
source bin/activate # activate the environment
pip install -r requirements.txt # install dependencies
make devserver # launch a local Pelican devserver
```

3) Work on your post. Don't forget to save your changes!

4) Commit your changes

```shell
git add .
git commit -m "new post about git"
```

5) and push your changes to the central repository

```shell
git push gonzalosaenz.com
```

# Final thoughts

You can get help for each git command by running for example:

```shell
git add --help # this will list help for git add
```

In the [references](#references) section you will find links to git resources.

There are a few things that I didn't cover in this entry. Like how to create a [pelican][] blog. I might or might not cover this in a future post.

# References <a name="references"></a>

Bellow you will find some git resources

* [Setting up a repository - bitbucket][bitbucket_repo]
* [How to set up a git repository locally and on a remote server][remote_repo]
* [Git ignore generator][git_ignore]

That's all folks! <br/>
Gonzalo S??enz

<!-- Links -->

[git_repository]: /images/git_repository.png
[bitbucket_repo]: https://www.atlassian.com/git/tutorials/setting-up-a-repository
[remote_repo]: http://blog.davidecoppola.com/2016/12/how-to-set-up-a-git-repository-locally-and-on-a-remote-server/
[git_ignore]: https://www.gitignore.io/?templates=python "Git ignore for python projects"

[github]: https://github.com
[gitlab]: https://gitlab.com
[bitbucket]: https://bitbucket.org
[pelican]: https://getpelican.com
