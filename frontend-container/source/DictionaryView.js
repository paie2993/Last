import { TreeView } from '@mui/x-tree-view';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import { Paper } from '@mui/material';
import { buildSingleWordList } from './SingleWord';


export default function DictionaryView(props) {

    const words = props.words
    const onWordActionClick = props.onWordActionClick
    const iconSupplier = props.iconSupplier

    return (
        <Paper className="display-line-break" sx={{
            p: 3,
            display: 'flex',
            flexDirection: 'column',
        }}>
            <TreeView
                aria-label="rich object"
                defaultCollapseIcon={<ExpandMoreIcon />}
                defaultExpanded={['root']}
                defaultExpandIcon={<ChevronRightIcon />}
                sx={{ flexGrow: 1, overflowY: 'auto' }}
            >
                {buildSingleWordList(words, onWordActionClick, iconSupplier)}
            </TreeView>
        </Paper>
    )
}