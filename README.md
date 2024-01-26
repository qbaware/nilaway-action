# Nilaway GitHub Action

[![GitHub Super-Linter](https://github.com/qbaware/nilaway-action/actions/workflows/linter.yml/badge.svg)](https://github.com/super-linter/super-linter)
![CI](https://github.com/qbaware/nilaway-action/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/qbaware/nilaway-action/actions/workflows/cd.yml/badge.svg)

This is a simple GitHub Action that checks Golang codebases for potential Nil panics.

## How To Use

### Define The Inputs

First, make sure to define the necessary input for the Action. You'd
have to provide a package that has to be scanned.

To do this, you can leverage GitHub
[variables](https://docs.github.com/en/actions/learn-github-actions/variables).
In short, go to your repository's `Settings` tab and add the variables under `Secrets and variables` then `Actions`.

### Modify Your Action

Add the following `deploy` job in your Action.

``` yaml
nil-check:
  # Assuming the `build` job builds the project,
  # we define a dependency on it.
  needs: build

  runs-on: ubuntu-latest
  steps:
    - name: Scan using nilaway
      uses: qbaware/nilaway-action@v0
      with:
        package-to-scan: "./..."
```

### That's It 🎉

### Sample Workflow View

![Sample workflow](/resources/sample-workflow.png)
