import { Grid } from '@mui/material'
import React, { useEffect } from 'react'
import './text.css'
import { useLocation } from 'react-router-dom'
import { useState } from 'react'
import { TextContent } from './TextContent'
import DictionaryView from './DictionaryView'
import AddIcon from '@mui/icons-material/Add';

const url = "http://localhost:5000"
const add_word_to_user_dictionary_url = `${url}/user/dictionary/add`

// on the left, the complete text
// on the right, the unknown words
export default function TextPage() {

    const location = useLocation()
    const title = location.state.title

    const text_content_url = `${url}/texts/content/${title}`
    const definitions_url = `${url}/texts/definitions/${title}`

    const [text, setText] = useState('')
    const [lemmas, setLemmas] = useState([])

    useEffect(() => {
        fetch(text_content_url)
            .then(data => data.text())
            .then(data => setText(data))
    }, [text_content_url])

    useEffect(() => {
        fetch(definitions_url)
            .then(data => data.json())
            .then(data => setLemmas(data))
    }, [definitions_url])

    function onWordActionClick(word) {
        if (!word?.name) {
            return
        }
        const url = `${add_word_to_user_dictionary_url}/${word.name}`
        fetch(url).then(_ => {
            const index = lemmas.findIndex((element) => element.name === word.name)
            const wordsPosDefinitionsCopy = lemmas.slice()
            wordsPosDefinitionsCopy.splice(index, 1)
            setLemmas(wordsPosDefinitionsCopy)
        })
    }

    return (
        <Grid container spacing={2}>
            <Grid item xs={6}>
                <TextContent text={text} />
            </Grid>
            <Grid item xs={6}>
                <DictionaryView
                    words={lemmas}
                    onWordActionClick={onWordActionClick}
                    iconSupplier={() => <AddIcon />}
                />
            </Grid>
        </Grid>
    )
}