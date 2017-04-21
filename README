# cmd-test
Run sequential or parallel commands and check their outputs.

#### Sample config:

Create a config file `myconf.json`
```json
{
  "actions": [{
    "command": "ls -lh {@} | awk '{print $5}' | tail -n1",
    "process": 1,
    "thread": 3,
    "io": [
      ["R:~/.vimrc", "X:d+", 2, 0],
      ["R:INVALID_FILE", "X:*No such file*", 1, 1]
    ]
  }]
}

```
Then run `cmd-test`:
```commandline
cmd-test myconf.json --report table --color
```

#### Config Parameters:

`actions`: list of all commands.
`command`: terminal command. Your replacement variable in `io` has `{@}` structure.
`process`: number of process which will be created during execution.
`thread`: number of thread which will be created during execution.
`io`: list of sample input/output which will be tested on the command:
`input`, `output`, `try_times`, `try_on_failed`

####Key patterns in input/output:

| Key   | Description                      |
| :---: | ---                              |
| `R`   | row data                         |
| `X`   | regular expression (regex)       |
| `M`   | math operation                   |
| `T`   | other threads input/output       |
| `P`   | other process input/output       |
| `D`   | distributed process input/output |

####List of exit codes:

| Exit code | Description                         |
| :---:     | ---                                 |
| `0`       | Success                             |
| `1`       | Missing config file                 |
| `2`       | Config file not found               |
| `3`       | Config file has no read permission  |
| `4`       | Config file content is invalid      |
| `5`       | Config file structure is not valid  |
