/*
 *	Logger Library by Parra Studios
 *	Copyright (C) 2016 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
 *
 *	A generic logger library providing application execution reports.
 *
 */

#ifndef LOG_PREPROCESSOR_H
#define LOG_PREPROCESSOR_H 1

/* -- Headers -- */

#include <log/log_api.h>

#include <preprocessor/preprocessor_if.h>
#include <preprocessor/preprocessor_arguments.h>
/*#include <preprocessor/preprocessor_for.h>*/

#ifdef __cplusplus
extern "C" {
#endif

/* -- Definitions -- */

#define LOG_PREPROCESSOR_LINE ((size_t) __LINE__)

/* -- Macros -- */

/*
#define log_configure(name, ...) \
	prerprocessor_foreach(__VA_ARGS__)
*/
#define log_write(name, level, message, ...) \
	PREPROCESSOR_IF(PREPROCESSOR_ARGS_COUNT(__VA_ARGS__),
		log_write_impl_va(name, LOG_PREPROCESSOR_LINE, log_record_function(), __FILE__, level, message, __VA_ARGS__), \
		log_write_impl(name, LOG_PREPROCESSOR_LINE, log_record_function(), __FILE__, level, message) \
	)

#ifdef __cplusplus
}
#endif

#endif /* LOG_PREPROCESSOR_H */
