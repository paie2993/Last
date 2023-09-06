import { TreeItem } from "@mui/x-tree-view"
import { buildDefinitionsList } from "./SingleDefinition"
import Box from "@mui/material/Box"
import Typography from '@mui/material/Typography';

function optionalOrigins(origins) {
    if (!origins) {
        return <Box></Box>
    }

    return (
        <Box sx={{ fontStyle: 'italic' }}>{origins.join(', ')}</Box>
    )
}

function computePartOfSpeechLabel(partOfSpeech) {
    const tag = partOfSpeech.tag
    const origins = partOfSpeech.origins

    return (
        <Typography component="span" sx={{ display: 'flex', flexDirection: 'row' }}>
            <Box sx={{ fontWeight: 'bold', m: 1 }} >{tag}</Box>
            {optionalOrigins(origins)}
        </Typography>
    )
}

export function SinglePartOfSpeech(props) {

    const wordName = props.wordName
    const partOfSpeech = props.partOfSpeech
    const treeItemLabel = computePartOfSpeechLabel(partOfSpeech)
    const definitions = partOfSpeech.definitions

    return (
        <TreeItem nodeId={wordName.concat(partOfSpeech.tag)} label={treeItemLabel}>
            {buildDefinitionsList(definitions)}
        </TreeItem>
    )
}

export function buildSinglePartOfSpeechList(wordName, partsOfSpeech) {
    return partsOfSpeech?.map((partOfSpeech) => {
        return <SinglePartOfSpeech key={wordName.concat(partOfSpeech.tag)} wordName={wordName} partOfSpeech={partOfSpeech}></SinglePartOfSpeech>
    })
}