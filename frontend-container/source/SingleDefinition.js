import { TreeItem } from '@mui/x-tree-view'

function indexDefinition(index, definition) {
    return `${index}. ${definition}`
}

export function SingleDefinition(props) {
    const index = props.index
    const definition = props.definition
    const formattedLabel = indexDefinition(index, definition)
    return <TreeItem nodeId={definition} label={formattedLabel} />
}

export function buildDefinitionsList(definitions) {
    return (
        definitions?.map((definition, index) => <SingleDefinition key={definition} index={index + 1} definition={definition} />)
        ?? <div />
    )
}