import { Box, Button, Typography } from '@mui/material';
import { styles } from './App.styles';

function App() {
  return (
    <Box sx={styles.page}>
      <Box
        component="img"
        src="https://picsum.photos/200"
        sx={styles.image}
      />
      <Typography variant="h3" component="h1" sx={styles.title}>
        Willkommen!
      </Typography>

      <Button
        variant="contained"
        color="primary"
        onClick={() => alert('Hallo aus React!')}
      >
        Klick mich
      </Button>

    </Box>
  );
}

export default App;