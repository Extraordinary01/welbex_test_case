<template>
	<div class="form-check">
		<input
			class="form-check-input"
			type="radio"
			:name="name"
			:id="id"
			@change="$emit('update:modelValue', id)"
		/>
		<label class="form-check-label" :for="id"> {{ label }} </label>
	</div>
</template>

<script>
	export default {
		props: {
			label: String,
			name: String,
			id: String,
			modelValue: String,
		},
	};
</script>
