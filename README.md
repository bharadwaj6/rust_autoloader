Rust Autoloader
================

[![Downloads](https://pypip.in/download/rust-autoloader/badge.svg)](https://pypi.python.org/pypi/rust-autoloader/)
[![Supported Python versions](https://pypip.in/py_versions/rust-autoloader/badge.svg)](https://pypi.python.org/pypi/rust-autoloader/)


This script detects any changes made to the rust files (`.rs`)
in current working directory and serves as an *autoloader* for your development.

Use this when you are learning rust/testing/editing rust files and
you're tired of doing `rustc test.rs` and `./test` over and over again.

Installation
=============

    $ pip install rust-autoloader

Usage
======

    from rust_autoloder import run
    run("path-to-working-directory")

You can also take the `autoloader.py` script and keep it running in the working
directory using `python autoloader.py` while working.

NOTE
=====

* This script is not meant to be any kind of substitute for `cargo build`.  Use this only when you're toying on some `.rs` files and don't use it in any serious project.
<br/>
* Doesn't play well with compiler warnings (yet). (One has to execute manually if warnings are generated).
<br/>
* Not possible to pass input to your rust program (yet).
