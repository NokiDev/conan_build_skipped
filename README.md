# Conan install won't call build if a previous one with same build_id failed.

Issue Reference : https://github.com/conan-io/conan/issues/2879

## Brief 

When using build_id method in a conanfile in order to have one build for n package.
If the build fails, conan won't remove the build directory, so in the further conan install, conan will consider the build as success as the build directory is present.

## How to reproduce : 

### Configuration used : 

- Os : Windows 10
- Arch : x64
- conan version : 1.7.4
- python version : 3.6
- cmake version : 3.11

### Test (Weird / Unwanted Behaviour)

Run 

```
conan create . user/channel
```
build() should failed without calling cmake.build (return -1).

Re run 
```
conan create . user/channel
```

build method is not called anymore, package method is called directly.

### Wanted Behaviour 

Conan need to clean build directory if the build fails or to check something else than build existance + build_id method presence to skip the build.
