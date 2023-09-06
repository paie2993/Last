import Box from "@mui/material/Box"
import IconButton from "@mui/material/IconButton"
import { TreeItem } from "@mui/x-tree-view"
import { buildSinglePartOfSpeechList } from "./SinglePartOfSpeech"

export function SingleWord(props) {

    const word = props.word
    const onWordActionClick = props.onWordActionClick
    const iconSupplier = props.iconSupplier

    const wordName = word?.name ?? ""
    const partsOfSpeech = word?.partsOfSpeech ?? []

    return (
        <Box sx={{
            p: 0.5,
            height: 'auto',
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'baseline',
        }}>
            <IconButton onClick={() => onWordActionClick(word)}>
                {iconSupplier()}
            </IconButton>
            <TreeItem nodeId={wordName} label={wordName} sx={{
                p: 1,
                flexGrow: 1
            }}>
                {buildSinglePartOfSpeechList(wordName, partsOfSpeech)}
            </TreeItem>
        </Box>
    )
}

export function buildSingleWordList(words, onWordActionClick, iconSupplier) {
    return words?.map((word, index) => {
        return <SingleWord key={word?.name ?? index}
            word={word}
            onWordActionClick={onWordActionClick} 
            iconSupplier={iconSupplier}
            />
    }) ?? <div />
}