"""
Note: I'm not 100% sure this works and haven't tested extensively. 
Let me know if you can break it!

The idea is to use the `pre` set for cycle detection. Parent nodes whose
children are in the process of being recursively expanded are added to
this set. If at any time a node is visted while in this set, a dependency 
cycle has been detected and we can report false.

After all children of a node have been expanded and have been shown to be 
acyclic, there is no point in re-searching this branch of the graph again. 
This optimization is supported by `post`, which stores fully expanded 
acyclic packages.

Furthermore, portions of the graph that have nothing to do with the 
dependency chain are left unvisited and unprocessed.

Follow-ups include returning the full dependency path or cycle.

This could also be solved with a topological sort.
"""

def can_install(package, dependencies):
    def can_install_r(package):
        if package in pre:
            return False
        elif package not in post:
            pre.add(package)
    
            for neighbor in dependencies[package]:
                if not can_install_r(neighbor):
                    return False
                    
            pre.remove(package)
            post.add(package)
    
        return True

    pre = set()
    post = set()
    return can_install_r(package)


if __name__ == "__main__":
    print(can_install("a", {"a": ["b", "c"], "b": ["c"], "c": []}))
    print(can_install("a", {"a": ["b", "c"], "b": ["c"], "c": ["a"]}))
    print(can_install("a", {"a": ["b", "c"], "b": ["c"], "c": ["b"]}))
    print(can_install("a", {"a": ["b", "c", "d"], "b": ["c"], "c": ["d"], "d": [], "x": ["b"]}))
