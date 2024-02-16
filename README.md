
# Servus RPM

---

### Introduction

This is a simple Hello World, which is compiled and then packaged into an RPM.

---

### Usage


To use this, you will need to ensure you have the rpm build tools:

    sudo dnf install rpmdevtools rpmlint

Then setup the RPM build environment by doing:

    rpmdev-setuptree

From here, you should have a folder in your home directory called rpmbuild

In this directory there are the following folders:

    BUILD  
    BUILDROOT  
    RPMS  
    SOURCES  
    SPECS  
    SRPMS

You will want to move the Servus folder from this directory to the SOURCES directory.

    cp -r ./Servus ~/rpmbuild/SOURCES/

Then copy the spec file to SPECS.

    cp ./Servus.spec ~/rpmbuild/SPECS/

From here, you will want to run rpmbuild from the SPECS directory.

    cd ~/rpmbuild/SPECS

Run RPMBUILD:

    rpmbuild -ba Servus.spec

-b is for build
-a is for target, which would be our .spec file.

---

### Installing RPM / Removing RPM

At this point, in the rpmbuild/RPMS folder, we should have an architecture type, and in that folder
we should have our RPM.

We simple cd to that folder and then run:

    sudo dnf install ./Servus 

(and then press tab) 

This will then install Servus.

We can run Servus by doing:

    $Servus
    Servus!
    $

To Remove, we simply do:

sudo dnf remove Servus

---


