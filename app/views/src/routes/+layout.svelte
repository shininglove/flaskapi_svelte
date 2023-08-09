<script>
    import "@skeletonlabs/skeleton/themes/theme-seafoam.css";
    import "@skeletonlabs/skeleton/styles/skeleton.css";
    import "../app.postcss";
    import { browser } from "$app/environment";
    import { QueryClient, QueryClientProvider } from "@tanstack/svelte-query";
    const queryClient = new QueryClient({
        defaultOptions: {
            queries: {
                enabled: browser,
            },
        },
    });
</script>

<QueryClientProvider client={queryClient}>
    <slot />
</QueryClientProvider>
