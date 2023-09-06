import { Paper } from "@mui/material"
import { useEffect, useState } from "react"
import './index.css'
import Typography from '@mui/material/Typography';
import SearchIcon from '@mui/icons-material/Search';
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import InputAdornment from "@mui/material/InputAdornment";
import DictionaryView from "./DictionaryView";
import AddIcon from '@mui/icons-material/Add';

const url = 'http://localhost:5000'
const dictionary_url = `${url}/dictionary`
const add_word_to_user_dictionary_url = `${url}/user/dictionary/add`

function sortLexicographically(dictionary) {
    return dictionary?.sort((a, b) => {
        const first = a?.name?.toUpperCase() ?? ""
        const second = b?.name?.toUpperCase() ?? ""
        if (first < second) {
            return -1
        } else {
            return 1
        }
    }) ?? 0
}

function filterByText(text, dictionary) {
    return dictionary.filter((word) => word?.name?.includes(text) ?? false)
}

function onWordActionClick(word) {
    if (!word?.name) {
        return
    }
    const url = `${add_word_to_user_dictionary_url}/${word.name}`
    fetch(url)
}

export default function Dictionary() {

    const [dictionary, setDictionary] = useState([])
    const [filtered, setFiltered] = useState([])

    useEffect(() => {
        fetch(dictionary_url)
            .then(data => data.json())
            .then(data => {
                if (!data) {
                    return
                }
                const sortedDictionary = sortLexicographically(data)
                setDictionary(sortedDictionary)
                setFiltered(sortedDictionary)
            })
    }, [])

    return (
        <Paper className="display-line-break" sx={{
            p: 3,
            display: 'flex',
            flexDirection: 'column'
        }}>
            <Box sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                justifyContent: 'space-around'
            }}>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1 }}
                >
                    Dictionary
                </Typography>
                <TextField
                    id="search-by-text"
                    label="Search"
                    variant="standard"
                    onChange={(event) => setFiltered(filterByText(event.target.value, dictionary))}
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <SearchIcon />
                            </InputAdornment>
                        ),
                    }}
                />
            </Box>
            <DictionaryView
                words={filtered}
                onWordActionClick={onWordActionClick}
                iconSupplier={() => <AddIcon />}
            />
        </Paper>
    )
}