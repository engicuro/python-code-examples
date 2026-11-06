"""Program to implement topological sorting.

Topological sorting arranges items in a sequence where
if item A must come before item B, then A appears before B.
Think of it like scheduling tasks where some tasks depend on others.

Example graph:
  A --> C --> E
  B --> C, D --> F
"""

def topological_sorting():
    """Perform topological sort on a directed acyclic graph."""
    # Our graph: each key is a task, and its value is a list of tasks that depend on it
    graph = {}
    graph['A'] = ['C']      # A must be done before C
    graph['B'] = ['C', 'D'] # B must be done before C and D
    graph['C'] = ['E']      # C must be done before E
    graph['D'] = ['F']      # D must be done before F
    graph['E'] = []         # E has no dependents
    graph['F'] = []         # F has no dependents

    # Count how many tasks must be completed before each task (in-degree)
    in_degree = {}
    all_nodes = set(graph.keys())
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
            all_nodes.add(neighbor)

    # Start with tasks that have no prerequisites (in-degree = 0)
    queue = []
    for node in all_nodes:
        if in_degree.get(node, 0) == 0:
            queue.append(node)

    result = []  # This will hold our sorted order

    # Process tasks one by one
    while queue:
        # Take the first task with no remaining prerequisites
        node = queue.pop(0)
        result.append(node)

        # For each task that depends on this one,
        # reduce its prerequisite count
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) - 1
            # If all prerequisites are now met, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    print(f"Topological sort order: {result}")
    return result

# Run the function when this file is executed
if __name__ == "__main__":
    topological_sorting()
