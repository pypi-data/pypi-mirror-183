def all_against_all(func, iterable, ignore_exceptions=True, skip_own=True):
    for i in range(len(iterable)):
        try:
            erga = []
            for k in range(len(iterable)):
                if skip_own:
                    if k == i:
                        continue
                try:
                    erga.append(
                        ((iterable[i], iterable[k]), func((iterable[k]), (iterable[i])))
                    )
                except Exception as fa:
                    if not ignore_exceptions:
                        raise fa
                    continue
            yield erga
        except Exception as fe:
            if not ignore_exceptions:
                raise fe
            continue


