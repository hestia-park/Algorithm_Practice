class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []

        for component in components:
            if component == "..":
                if stack:  # Pop only if the stack is not empty
                    stack.pop()
            elif component == "." or component == "":
                # Ignore '.' and empty components
                continue
            else:
                # Valid directory or file name
                stack.append(component)

        # Construct the canonical path
        return "/" + "/".join(stack)
                