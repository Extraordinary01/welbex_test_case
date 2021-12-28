<template>
	<suspense>
		<template #default>
			<Async />
		</template>
		<template #fallback>
			<div class="loader"></div>
		</template>
	</suspense>
</template>

<script>
	import Async from "@/views/Async.vue";
	export default {
		components: {
			Async,
		},
	};
</script>
