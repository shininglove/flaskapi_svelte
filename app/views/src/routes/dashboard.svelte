<script lang="ts">
    import { createQuery } from "@tanstack/svelte-query";
    import { createZodFetcher } from "zod-fetch";
    import {
        type infoType,
        info,
        type dataArrayType,
        dataArray,
    } from "$lib/query";
    import Banner from "./banner.svelte";
    const fetchWithZod = createZodFetcher();
    const infoAPI = createQuery<infoType, Error>({
        queryKey: ["info"],
        queryFn: async () => await fetchWithZod(info, `/info`),
    });
    const dataAPI = createQuery<dataArrayType>({
        queryKey: ["full_info"],
        queryFn: async () => await fetchWithZod(dataArray, `/data`),
    });
</script>

<div class="font-extrabold text-4xl mt-2 mb-4">Dashboard</div>
<section class="w-full flex">
    <select
        class="select w-auto px-4 mr-2 bg-primary-300 text-surface-700"
        id="categories"
    >
        {#if $infoAPI.isSuccess}
            {#each $infoAPI.data.categories as item}
                <option value={item}>{item}</option>
            {/each}
        {/if}
    </select>
    <input
        class="input px-4 max-w-xl bg-primary-300 text-surface-700"
        type="search"
        name="lookup"
        placeholder="Search..."
    />
</section>
<section class="w-full flex">
    {#if $dataAPI.isSuccess}
        <Banner size={$dataAPI.data.length} source={$dataAPI.data} />
    {:else if $dataAPI.isLoading}
        <p>loading...</p>
    {:else if $dataAPI.error}
        <p class="text-red-600">{$dataAPI.error}</p>
    {/if}
</section>
