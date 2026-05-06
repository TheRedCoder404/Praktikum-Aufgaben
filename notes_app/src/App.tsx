import {type KeyboardEvent, useState} from "react";
import {Box, Button, Divider, Paper, TextField, Typography,} from "@mui/material";

type Note = {
    text: string;
    createdAt: Date;
}

function formatTimestamp(date: Date): string {
    return date.toLocaleString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    });
}

export function App() {
    const [input, setInput] = useState("");
    const [notes, setNotes] = useState<Note[]>([]);

    function addNote() {
        const text = input.trim();
        if (!text) return;
        setNotes([
            { text, createdAt: new Date()},
            ...notes,
        ])
        setInput("");
    }

    function handleKeyDown(e: KeyboardEvent) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            addNote();
        }
    }

    return (
        <Box sx={{width: "100vw", display: "flex", justifyContent: "center", p: 2}}>
            <Paper
                elevation={4}
                sx={{
                    width: "100%",
                    maxWidth: 480,
                    p: 3,
                    display: "flex",
                    flexDirection: "column",
                    gap: 2,
                }}
            >
                <Typography variant="h6" fontWeight={600}>
                    Nottes
                </Typography>

                <TextField
                    multiline
                    minRows={3}
                    maxRows={8}
                    fullWidth
                    placeholder="Write an note…"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyDown}
                />

                <Button variant="contained" onClick={addNote} disabled={!input.trim()}>
                    Addition of the Note
                </Button>

                {notes.length > 0 && (
                    <Box sx={{display: "flex", flexDirection: "column", gap: 1.5, mt: 1}}>
                        <Divider/>
                        {notes.map((note, index) => (
                            <Box key={'note-' + (notes.length - index)}>
                                <Typography variant="body1" sx={{whiteSpace: "pre-wrap"}}>
                                    {note.text}
                                </Typography>
                                <Typography variant="caption" color="text.secondary">
                                    {formatTimestamp(note.createdAt)}
                                </Typography>
                            </Box>
                        ))}
                    </Box>
                )}
            </Paper>
        </Box>
    );
}

export default App;
