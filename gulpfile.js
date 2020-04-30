const { src, task, series, dest,watch } = require("gulp")
const jsonlint = require("gulp-jsonlint")
const zip = require("gulp-zip")
const request = require("request")

task("json", async () => {
	await src(["./assets/**/*.json", "pack.mcmeta"])
		.pipe(jsonlint())
		.pipe(jsonlint.failOnError())
		.pipe(jsonlint.reporter())
})
task("zip", async () => {
	await src(["**/assets/**", "pack.*"])
		.pipe(zip("rails-3d.zip", { compress: true }))
		.pipe(dest("."))
})

task("watch", ()=>{
	watch(["assets/**/models/block/*/_*.json","assets/**/models/block/_*.json"],async()=>{
	})
})
task("upload", async () => {
	// ToDo
})

exports.default = series("json", "zip")
