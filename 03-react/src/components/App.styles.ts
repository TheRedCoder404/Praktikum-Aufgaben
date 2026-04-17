import type { SxProps, Theme } from '@mui/material';

export const styles: Record<string, SxProps<Theme>> = {
  page: {
    minHeight: '100vh',
    backgroundColor: '#2d2d2d',
    color: '#ffffff',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 4,
  },

  image: {
    width: 200,
    height: 200,
  },

  title: {
    marginBottom: 2,
  },
};