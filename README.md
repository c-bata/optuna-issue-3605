# Optuna Issue 3605

https://github.com/optuna/optuna/issues/3605

## Step to reproduce

Prepare a Python environment.

```
$ python3.8 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Execute a shell script to reproduce the bug.

```
$ ./test_postgresql_order.sh
...

python example.py
[I 2022-06-08 10:00:04,328] A new study created in RDB with name: no-name-fe132448-7fdf-4c38-9a59-aa5611fc252e
[I 2022-06-08 10:00:04,545] Trial 0 finished with value: 6509.35468355771 and parameters: {'x': 80.68676894979566, 'y': -1}. Best is trial 0 with value: 6509.35468355771.
[I 2022-06-08 10:00:04,678] Trial 1 finished with value: 2255.1446289317128 and parameters: {'x': -47.49889081790977, 'y': -1}. Best is trial 1 with value: 2255.1446289317128.
[I 2022-06-08 10:00:04,786] Trial 2 finished with value: 6215.957053977707 and parameters: {'x': 78.84768261640735, 'y': -1}. Best is trial 1 with value: 2255.1446289317128.
[I 2022-06-08 10:00:04,908] Trial 3 finished with value: -0.4226857153793956 and parameters: {'x': 0.7598120061045393, 'y': -1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,031] Trial 4 finished with value: 3037.5199827529195 and parameters: {'x': -55.10462759835075, 'y': 1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,157] Trial 5 finished with value: 6567.853338849351 and parameters: {'x': -81.03612366623511, 'y': 1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,286] Trial 6 finished with value: 2224.548011208507 and parameters: {'x': 47.15451209808566, 'y': 1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,404] Trial 7 finished with value: 7954.292436683009 and parameters: {'x': 89.19244607410994, 'y': -1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,529] Trial 8 finished with value: 20.05114235824884 and parameters: {'x': 4.364761431997039, 'y': 1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,675] Trial 9 finished with value: 4878.94958438663 and parameters: {'x': -69.85663593665694, 'y': -1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,803] Trial 10 finished with value: 8.99239351941829 and parameters: {'x': -2.9987319852594845, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:05,927] Trial 11 finished with value: 44.348844323820686 and parameters: {'x': -6.659492797790286, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,057] Trial 12 finished with value: 2.616557950356071 and parameters: {'x': 1.6175778034938755, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,179] Trial 13 finished with value: 849.360507860521 and parameters: {'x': 29.143790210961253, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,329] Trial 14 finished with value: 1115.8944361446668 and parameters: {'x': -33.405006153938466, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,447] Trial 15 finished with value: 1068.5556749114485 and parameters: {'x': 32.68876985925669, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,565] Trial 16 finished with value: 739.4461417687749 and parameters: {'x': -27.192758995158524, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,702] Trial 17 finished with value: 285.0587446986398 and parameters: {'x': 16.913271259535804, 'y': -1}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,825] Trial 18 finished with value: 3176.3341620785336 and parameters: {'x': 56.35897587854603, 'y': 0}. Best is trial 3 with value: -0.4226857153793956.
[I 2022-06-08 10:00:06,938] Trial 19 finished with value: 9487.144930451354 and parameters: {'x': -97.40710923978472, 'y': -1}. Best is trial 3 with value: -0.4226857153793956.
Print the order of trial's number
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```