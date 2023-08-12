<script lang="ts">
    import type { dataArrayType } from "$lib/query";
    import {
        Paginator,
        Table,
        type PaginationSettings,
    } from "@skeletonlabs/skeleton";
    export let size: Number;
    export let source: dataArrayType;
    //const host: string = import.meta.env.VITE_HOST_URL;
    let page = {
        offset: 0,
        limit: 5,
        size,
        amounts: [5, 9, 12],
    } as PaginationSettings;

    const headers = ["category", "amount", "description", "date"];

    function dataSplicer(
        data: dataArrayType,
        page: PaginationSettings
    ) {
        const output = data.flatMap((d) =>
            d.map((n) => [
                n.category,
                n.amount,
                n.description,
                new Date(n.date).toLocaleDateString(),
            ])
        ).sort((a,b) => Number(b[1]) - Number(a[1]));
        // ^choosing the amount column
        const items = output.slice(
            page.offset * page.limit, // start
            page.offset * page.limit + page.limit // end
        );
        return items;
    }

    $: simpleTable = dataSplicer(source, page);

</script>

<section class="w-full mt-5">
    {#if source}
        <Table source={{ head: headers, body: simpleTable }} />
        <br class="mb-1" />
        <Paginator
            bind:settings={page}
            showFirstLastButtons={true}
            showPreviousNextButtons={true}
        />
    {/if}
</section>
