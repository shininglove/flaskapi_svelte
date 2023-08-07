<script lang="ts">
    import { onMount } from "svelte";
    import { z } from "zod";
    import { createZodFetcher } from "zod-fetch";

    const host: string = import.meta.env.VITE_HOST_URL;

    const fetchWithZod = createZodFetcher();

    export let info: Promise<string> | null;

    onMount(async () => {
        info = dataFetcher();
    });

    async function dataFetcher() {
        const res = await fetchWithZod(
            z.object({ hello: z.string() }),
            `${host}/data`
        );
        console.log(res);
        return res.hello;
    }

</script>

<section>
    <div>About</div>
    <div>Element goes zzzooommm!</div>
    {#await info}
        <p>loading...</p>
    {:then myInfo}
        {#if myInfo}
            <p>The info is: {myInfo}</p>
        {/if}
    {:catch error}
        <p style="color: red;">{error.message}</p>
    {/await}
</section>
