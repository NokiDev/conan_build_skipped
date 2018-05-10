# Conan install won't call build if a previous one with same build_id failed.

Issue Reference : https://github.com/conan-io/conan/issues/2879

## Brief 

When using build_id method in a conanfile in order to have one build for n package.
If the build fails, conan consider the build as success and will skip it for further conan install.


## How to reproduce : 

### Configuration used : 

- Os : Windows 10
- Arch : x64
- conan version : 1.3.2
- python version : 2.7
- cmake version : 3.11

### First Test (Weird / Unwanted Behaviour)

Run 

```
conan export . user/channel
```

```
conan install MyProject/1.0@user/channel --build
```

build() should failed.

Re run 
```
conan install MyProject/1.0@user/channel --build
```

build method is not called anymore, package method is called directly.

### Second Test (Normal / Wanted Behaviour)

Edit conanfile.py and comment build_id method

Then run 
```
conan export . user/channel
```

```
conan install MyProject/1.0@user/channel --build
```

build() should failed.

Re run 
```
conan install MyProject/1.0@user/channel --build
```

build method is called normally and fails again.