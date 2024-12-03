# aoc-2024

## Set Year
- Set `AOC_YEAR` variable in [.env](.env) to current year

## Set Session Token 
- go to https://adventofcode.com/ 
- make sure you are logged in
- open devtools
- copy value of `session` cookie
- paste into `AOC_SESSION` variable in [.env](.env)

## Start New Day
- creates base files for day from templates
- downloads input file from adventofcode.com
```
$ pipenv run new {day}

example:
$ pipenv run new 1
```

## Set Test Data
- create files in the `inputs` folder for each sample data provided
- add the samples to the `test_inputs` method in `Day{day}Part{part}Controller` with filename and expected result:
```python
def test_inputs(self) -> list[FileResult[AnswerType]]:
    return [FileResult("sample01.txt", 18)]
```
Failure to set test data will result in:
```
Exception: No sample files setup. Add these to: Day03PartAController
```
Failure to pass test data will result in:
```
Exception: Test Fail: Sample src/day03/input_sample01.txt, expecting: 0, actual: None
```

## Run Day Part
This will run the following for a specified day and part (a or b):
- Run all test data and verify correct result
- if successful, run the main input
- If the answer has not yet been found, it will then submit the main input result.
- Upon successful submission, the answer will be saved to `inputs/{part}_answer.txt`
- From now on, the main input will be treated as test data and not submitted
```
$ pipenv run part {day} {part}

example: 
$ pipenv run part 1 a
```

## Dry Run
In case you don't want to submit upon successful test execution
```
$ pipenv run dryrun {day} {part}

example: 
$ pipenv run dryrun 1 a
```

## Testing
Pytest is used for testing
```
$ pipenv run test
```

## Linting
Flake8 is used for linting
```
$ pipenv run lint
```

## Formatting
Black is used for formatting
```
$ pipenv run fmt
```

## Run all quality checks and auto-format
``` 
$ pipenv run checks 
``` 

## Install Pre-Commit hook to run all checks
```
$ pipenv run setup
```

## CI
Github Actions is used for CI

[CI Workflow on Github Actions](https://github.com/tom-haug/aoc-2022/actions/workflows/ci.yml)

[Pipeline Config](.github/workflows/ci.yml)
