<template>
	<Header />
	<div class="container-fluid table-container">
		<div class="row">
			<div class="col-lg-9">
				<table class="table">
					<thead>
						<tr>
							<th scope="col">Дата</th>
							<th scope="col">Название</th>
							<th scope="col">Количество</th>
							<th scope="col">Дистанция</th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="item in data.results" :key="item">
							<td>{{ item.date }}</td>
							<td>{{ item.name }}</td>
							<td>{{ item.amount }}</td>
							<td>{{ item.distance }}</td>
						</tr>
					</tbody>
				</table>
				<nav aria-label="Page navigation example" v-if="data.amount_pages > 1">
					<ul class="pagination">
						<li class="page-item" v-if="data.links.previous">
							<span class="page-link" @click="getPage(data.links.previous)"
								>Назад</span
							>
						</li>
						<li class="page-item" v-if="data.page - 2 > 1">
							<span class="page-link">...</span>
						</li>
						<li class="page-item" v-if="data.page - 2 > 0">
							<span
								class="page-link"
								@click="getPage(data.links.previous, data.page - 2)"
								>{{ data.page - 2 }}</span
							>
						</li>
						<li class="page-item" v-if="data.page - 1 > 0">
							<span class="page-link" @click="getPage(data.links.previous)">{{
								data.page - 1
							}}</span>
						</li>
						<li class="page-item active">
							<span class="page-link">{{ data.page }}</span>
						</li>
						<li class="page-item" v-if="data.page + 1 <= data.amount_pages">
							<span class="page-link" @click="getPage(data.links.next)">{{
								data.page + 1
							}}</span>
						</li>
						<li class="page-item" v-if="data.page + 2 <= data.amount_pages">
							<span
								class="page-link"
								@click="getPage(data.links.next, data.page + 2)"
								>{{ data.page + 2 }}</span
							>
						</li>
						<li class="page-item" v-if="data.page + 2 < data.amount_pages">
							<span class="page-link">...</span>
						</li>
						<li class="page-item" v-if="data.links.next">
							<span class="page-link" @click="getPage(data.links.next)"
								>Вперед</span
							>
						</li>
					</ul>
				</nav>
			</div>
			<div class="col-lg-3">
				<h4>Фильтер</h4>
				<div class="filter-column mb-4">
					<a
						class="btn"
						data-bs-toggle="collapse"
						href="#column"
						role="button"
						aria-expanded="false"
						aria-controls="column"
						style="background-color: #e3f2fd"
						>Выберите колонку <i class="bi bi-arrow-down"></i>
						<span class="arrow"></span
					></a>
					<ul class="sub-menu collapse mt-4" id="column">
						<li>
							<radio
								name="column"
								id="name"
								v-model="column"
								label="Название"
							></radio>
						</li>

						<li>
							<radio
								name="column"
								id="amount"
								v-model="column"
								label="Количество"
							></radio>
						</li>

						<li>
							<radio
								name="column"
								id="distance"
								v-model="column"
								label="Дистанция"
							></radio>
						</li>
					</ul>
				</div>
				<div class="filter-column mb-4">
					<a
						class="btn"
						data-bs-toggle="collapse"
						href="#condition"
						role="button"
						aria-expanded="false"
						aria-controls="condition"
						style="background-color: #e3f2fd"
						>Выберите условие <i class="bi bi-arrow-down"></i>
						<span class="arrow"></span
					></a>
					<ul class="sub-menu collapse mt-4" id="condition">
						<li>
							<radio
								name="condition"
								id="equal"
								v-model="condition"
								label="Равно ="
							></radio>
						</li>

						<li>
							<radio
								name="condition"
								id="contains"
								v-model="condition"
								label="Содержит"
							></radio>
						</li>

						<li>
							<radio
								name="condition"
								id="greater"
								v-model="condition"
								label="Больше >"
							></radio>
						</li>
						<li>
							<radio
								name="condition"
								id="lower"
								v-model="condition"
								label="Меньше <"
							></radio>
						</li>
					</ul>
				</div>
				<div class="filter-column">
					<div class="input-group">
						<input
							type="text"
							class="form-control"
							placeholder="Введите значение для фильтрации"
							aria-label="filter"
							aria-describedby="addon-wrapping"
							v-model="value"
						/>
					</div>
				</div>
				<div class="filter-column mt-4">
					<button type="button" class="btn btn-success" @click="filter">
						Отфильтровать
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Header from "@/components/Header.vue";
	import Radio from "@/components/ui/Radio.vue";
	import api from "@/api/api";
	import { ref } from "vue";
	export default {
		components: {
			Header,
			Radio,
		},
		async setup() {
			const getData = async (url) => {
				const response = await api.get(url);
				return response.data;
			};
			const data = ref({});
			data.value = await getData("table/");
			const column = ref("");
			const condition = ref("");
			const value = ref("");
			const filter = async () => {
				const url =
					"table/?column=" +
					column.value +
					"&condition=" +
					condition.value +
					"&value=" +
					value.value;
				data.value = await getData(url);
			};
			const getPage = async (url, page = undefined) => {
				if (page) {
					let editedUrl = url;
					const pagePosition = editedUrl.indexOf("page");
					editedUrl =
						editedUrl.slice(0, pagePosition + 5) +
						page.toString() +
						editedUrl.slice(pagePosition + 5 + page.toString().length);
					data.value = await getData(editedUrl);
				} else {
					data.value = await getData(url);
				}
			};
			return {
				data,
				column,
				condition,
				value,
				filter,
				getPage,
			};
		},
	};
</script>

<style lang="scss">
	ul li {
		list-style: none;
	}
	.page-link {
		cursor: pointer;
	}
</style>
