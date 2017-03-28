Package managers
================

As you learn more about coding, you will find yourself having to install and
uninstall hundreds to thousands of small programs, called "packages" or "libraries".
If you install these the same way you install programs like MS Office
(e.g. download executable and run), you will overwhelm yourself very quickly.
Luckily, [package managers](http://en.wikipedia.org/wiki/Package_manager) exist.

### You already use package managers!

Have you ever installed an app on your phone, or a game through steam? If you
have, then you already use package managers.

![](img/managers.png)

Let's think through some of the advantages:

 * Centralized searching
 * One-click install and uninstall processes
 * Automatically installs the right version for your device
 * Easy to view all installed packages and versions
 * One-click "update all" functionality

Code package managers do all of this for you - and more! We'll focus on the
basic features here, but you should take the time to read up on the more advanced
topics when you get a chance.

### Any caveats?

While there has been a push to have only one package manager that controls
everything, the current state of programming is more divided. Most programming
languages come with their own specialized package managers, and each operating
system additionally has its own package manager. This means that you will
probably have a couple of package managers to handle. This is not as simple as
one manager, but it is still much better than installing everything manually. It's
no different than having to manage separate App Store, Google Play, and Steam
accounts.

Furthermore, not all packages are guaranteed to work through every package
manager. It's up to the package authors to determine which managers to
support or ignore. Large projects generally support everything, but small
domain-specific packages (like those commonly used in science) rarely support
every (or any) package manager. Resist the urge to give up when things get tough!

### Package managers you should know

Below, we will break package managers into language-specific and OS-specific. Wherever
possible, We're providing you the most popular way to do things without getting too
much into the *why*. From here, we'll install a package manager and walk through
its features.

##### Platform-specific package managers

These are package managers that are only available on one operating system. These
usually involve packages that need to be compiled, so expect to see a lot of
Fortran, C, and C++ libraries.

 * Linux: `apt-get` for Debian, `yum` for Red Hat, and more. Installed by default.
 * Mac: [Homebrew](http://brew.sh/) is the current standard.
 * Windows: [Chocolatey](https://chocolatey.org/) is fairly popular.

##### Language-specific package managers

Many other languages come with their own cross-platform package managers. It's
generally recommended to use these over platform-specific managers when possible.

 * Go: [get](https://golang.org/cmd/go/)
 * Julia: [Pkg](http://pkg.julialang.org/)
 * Rust: [cargo](http://doc.crates.io/)
 * Ruby: [gem](https://rubygems.org/)
 * R: [install.packages](http://ww2.coastal.edu/kingw/statistics/R-tutorials/package.html)
 * Python: [pip](https://docs.python.org/3/installing/)

##### Conda

[Conda](http://conda.pydata.org/docs/) is a package manager developed for scientists.
It's not platform specific, but it's not really language specific either.
Features include:

 * Cross platform
 * No root access required (great for older clusters!)
 * Python centric, but handles C, Fortran, R, and more
 * Uses pre-compiled packages for super-fast installs
 * Supports pip packages
 * Easy to swap programming language versions (e.g. Python 2 vs 3)

Conda is 1. interesting and 2. won't mess up your environment. In other words,
it's a great workshop package manager. Let's install it and see how it works.

### Workshop - installing conda

 * Go to [this site](http://conda.pydata.org/miniconda.html#miniconda) and download
   the Python 3 version for your OS.
 * Run it by either double-clicking or typing `bash Miniconda-*.sh`.
 * Make sure to select "yes" for every option.
 * To test, reboot your terminal and type `which python`. It should point to `~/miniconda3/bin/python`.

We can now use conda to install, uninstall, and upgrade packages in one-line
commands. Let's grab a couple of the most commonly used Python packages: [numpy](http://www.numpy.org/),
[ipython](http://ipython.org/), and [flake8](https://flake8.readthedocs.org/en/2.3.0/).
To install all of these packages, run the command:

```
conda install numpy ipython flake8
```

You should now be able to type `ipython` to enter an IPython terminal, `import numpy`
to use numpy's linked fortran libraries, and `flake8` to test your code against
a style guide.

Let's go back to our above list of package manager benefits, and show how we would
use conda in each scenario.

##### Centralized searching

`conda search django` will search for all packages with "django" in the name.

##### One-click install and uninstall processes

`conda install django` installs the [Django web framework](https://www.djangoproject.com/).
`conda remove django` removes it.

##### Automatically installs the right version for your device

When you typed `conda install django`, it grabbed the most recent version that
works with your OS, architecture, and python version. Much like google play,
it did it all without you noticing.

##### Easy to view all installed packages and versions

`conda list`. Pretty straightforward.

##### One-click "update all" functionality

`conda update --all` will go through every installed package, check for newer
versions, and update when needed.

### Moving forward

This is as far as we're going with package managers. Spend some time getting
comfortable with their basic usage, and then dive into the more advanced
features. Look into two topics in particular:

 * Virtual environments provide another layer of organization, and are especially
   useful if you have multiple simultaneous projects.
   [Here's a conda tutorial](http://www.continuum.io/blog/conda).
 * Making your projects installable through package managers. It's a good practice
   that allows you to easily share your project with others.
   [Here's a pip tutorial](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/).
 * For every language you use, read through the most installed packages. It's a good
   way to learn what's out there. [Here's a list for python](http://pypi-ranking.info/alltime).
