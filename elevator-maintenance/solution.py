def solution(l):
    splitter = [version.split(".") for version in l]
    mapping = [map(int, version) for version in splitter]
    sorter = sorted(mapping)
    joiner = []

    for versions in sorter:
        joiner.append([".".join(str(versions) for versions in version) for version in sorter])

    return joiner

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
