
def algo_player(name, description):
    def _on_game_over(fn):
        _algos[name] = AlgoMetaData(description=_algos[name].description,
                                    fn=_algos[name].fn,
                                    on_game_over=fn,
                                    on_start_game=_algos[name].on_start_game)
        return fn

    def _on_start_game(fn):
        _algos[name] = AlgoMetaData(description=_algos[name].description,
                                    fn=_algos[name].fn,
                                    on_game_over=_algos[name].on_game_over,
                                    on_start_game=fn)
        return fn

    def _algo(fn):
        if name in _algos:
            raise ValueError("Algo '{}' is already defined.".format(name))
        elif not ALLOWED_ALGO_NAME.match(name):
            raise ValueError("Algos can only have names containing letters,"
                             " numbers, space, underscore and hyphen.")
        elif _filename(fn) in {_filename(i.fn) for i in _algos.values()}:
            raise ValueError("You must put each algo in its own file.")
        else:
            _algos[name] = AlgoMetaData(description=description,
                                        fn=fn,
                                        on_game_over=None,
                                        on_start_game=None)
            fn.on_game_over = _on_game_over
            fn.on_start_game = _on_start_game
            return fn

    return _algo

def simulate_all_with_stats(boardsize, iterations, do_deepcopy=True):
    algos = _algos.keys()
    if len(algos) < 2:
        print("Only {} algo defined - can't simulate.".format(len(algos)))
        return []
    results = {algo: 0 for algo in algos}
    total_stats = {}
    print("Running simulation...")
    for algo_1, algo_2 in combinations(algos, 2):
        winners, stats = run_simulation(algo_1,
                                        algo_2,
                                        boardsize=boardsize,
                                        iterations=iterations,
                                        do_deepcopy=do_deepcopy)

        algo_1_wins = len(list(filter(lambda x: x == algo_1, winners)))
        algo_2_wins = len(winners) - algo_1_wins

        print("{}({}) vs {}({})".format(algo_1, algo_1_wins,
                                        algo_2, algo_2_wins))

        results[algo_1] += algo_1_wins
        results[algo_2] += algo_2_wins

        for algo in set(stats.keys()).intersection(total_stats.keys()):
            for col in total_stats[algo].keys():
                total_stats[algo][col] += stats[algo][col]
        for algo in set(stats.keys()) - set(total_stats.keys()):
                total_stats[algo] = stats[algo]

    return list(reversed(sorted(results.items(), key=lambda item: item[1]))), total_stats

def simulate_all(boardsize, iterations, do_deepcopy=True):
    return simulate_all_with_stats(boardsize, iterations, do_deepcopy)[0]




### PASTE YOUR ALGO CODE HERE




