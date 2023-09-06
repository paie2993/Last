import Paper from "@mui/material/Paper"
import Typography from "@mui/material/Typography"

export function TextContent(props) {

    const text = props.text ?? ''

    return (
        <Paper className="display-line-break" sx={{
            p: 3,
            display: 'flex',
            flexDirection: 'column',
        }}>
            <Typography align='justify'>
                {text}
            </Typography>
        </Paper>
    )
}