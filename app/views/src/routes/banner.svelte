<script lang="ts">
    import { createQuery } from "@tanstack/svelte-query";
    import { z } from "zod";
    import { createZodFetcher } from "zod-fetch";
    const fetchWithZod = createZodFetcher();
    //const host: string = import.meta.env.VITE_HOST_URL;
    const data = z.object({ hello: z.string() });
    const info = createQuery<z.infer<typeof data>, Error>({
        queryKey: ["info"],
        queryFn: async () => await fetchWithZod(data, `/data`),
    });
</script>
<div>
    {#if $info.isSuccess}
        <aside class="alert variant-filled-error">
            <i class="fa-solid fa-triangle-exclamation text-4xl" />
            <div class="alert-message">
                <h3 class="h3">Warning</h3>
                <p>{$info.data.hello}</p>
            </div>
            <div class="alert-actions">
                <button class="btn variant-filled">Hello</button>
            </div>
        </aside>
    {:else if $info.isLoading}
        <p>loading...</p>
    {:else if $info.error}
        <p class="text-red-600">{$info.error.message}</p>
    {/if}
</div>
