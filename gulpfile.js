const { src, task, series, dest } = require("gulp")
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
		.pipe(zip("rails-3d.zip", { compress: false }))
		.pipe(dest("."))
})

task("upload", async () => {
	// ToDo
})

exports.default = series("json", "zip")
