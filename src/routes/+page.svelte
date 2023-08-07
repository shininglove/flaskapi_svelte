<script lang="ts">
    import { createQuery } from "@tanstack/svelte-query";

    import { z } from "zod";

    import {createZodFetcher} from "zod-fetch";

    const fetchWithZod = createZodFetcher();

    const host: string = import.meta.env.VITE_HOST_URL;

    const data = z.object({ hello: z.string() });

    const info = createQuery<z.infer<typeof data>, Error>({
        queryKey: ["info"],
        queryFn: async () => await fetchWithZod(data,`${host}/data`),
    });

</script>

<section>
    <div>Home</div>
    <div>Element goes zzzooommm!</div>
    {#if $info.isLoading}
        <p>loading...</p>
    {:else if $info.isSuccess}
        <p>The info is: {$info.data.hello}</p>
    {:else if $info.error}
        <p style="color: red;">{$info.error.message}</p>
    {/if}
</section>
