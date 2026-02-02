import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      // Custom typography styles for code and math
      typography: (theme) => ({
        DEFAULT: {
          css: {
            maxWidth: 'none', // Allow text to fill container
            code: {
              color: theme('colors.blue.600'),
              backgroundColor: theme('colors.blue.50'),
              padding: '0.2em 0.4em',
              borderRadius: '0.25rem',
              fontWeight: '600',
            },
            'code::before': { content: '""' }, // Remove backticks
            'code::after': { content: '""' },
          },
        },
        invert: {
          css: {
            code: {
              color: theme('colors.blue.300'),
              backgroundColor: theme('colors.blue.900'),
            },
          },
        },
      }),
    },
  },
  plugins: [typography],
};