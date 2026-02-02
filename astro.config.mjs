// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import typography from '@tailwindcss/typography';

export default defineConfig({
  // This "integrations" line is what turns on the styling
  integrations: [tailwind()], 
  
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
    shikiConfig: {
      theme: 'dracula',
      wrap: true,
    },
  },

  plugins: [
    typography, // ✅ Use the variable
  ],
});