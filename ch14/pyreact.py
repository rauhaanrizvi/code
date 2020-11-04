# Load React and ReactDOM JavaScript libraries into local namespace
React = require('react')
ReactDOM = require('react-dom')

# Map React javaScript objects to Python identifiers
createElement = React.createElement
useState = React.useState


def render(root_component, props, container):
    def main():
        ReactDOM.render(
            React.createElement(root_component, props),
            document.getElementById(container)
        )

    document.addEventListener("DOMContentLoaded", main)


# JavaScript function mappings
alert = window.alert
