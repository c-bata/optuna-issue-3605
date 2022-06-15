import optuna
import time


def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    y = trial.suggest_categorical("y", [-1, 0, 1])
    time.sleep(0.20 - trial.number / 100)
    return x**2 + y


def main():
    storage = optuna.storages.RDBStorage("postgresql+psycopg2://root:root@localhost:5432/optuna")
    study = optuna.create_study(storage=storage)
    study.optimize(objective, n_trials=20, n_jobs=4)

    with storage.engine.connect() as connection:
        connection.execute("COMMIT")
        connection.execute("VACUUM ANALYZE trials")

    print("Print the order of trial's number")
    print([t.number for t in storage.get_all_trials(study_id=study._study_id)])


if __name__ == '__main__':
    main()
