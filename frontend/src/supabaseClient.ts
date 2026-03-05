import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

// Safety check to ensure variables are loading
if (!supabaseUrl || !supabaseAnonKey) {
  console.error("Supabase environment variables are missing! Check your .env file.");
}

// Configure Supabase client to handle OAuth hash fragment
// This is important for Google OAuth redirects
export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    // Automatically handle OAuth hash fragment
    // This tells Supabase to process the #access_token from OAuth redirect
    flowType: 'implicit',
    // Storage is not needed for this use case
    storage: {
      getItem: (key: string) => Promise.resolve(localStorage.getItem(key)),
      setItem: (key: string, value: string) => Promise.resolve(localStorage.setItem(key, value)),
      removeItem: (key: string) => Promise.resolve(localStorage.removeItem(key)),
    },
    // Auto-detect OAuth tokens in URL hash
    detectSessionInUrl: true,
  },
});
