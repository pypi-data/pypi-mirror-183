// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: graphscope/proto/types.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_graphscope_2fproto_2ftypes_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_graphscope_2fproto_2ftypes_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3021000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3021009 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
#include <google/protobuf/any.pb.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_graphscope_2fproto_2ftypes_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_graphscope_2fproto_2ftypes_2eproto {
  static const uint32_t offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_graphscope_2fproto_2ftypes_2eproto;
namespace gs {
namespace rpc {
class QueryArgs;
struct QueryArgsDefaultTypeInternal;
extern QueryArgsDefaultTypeInternal _QueryArgs_default_instance_;
}  // namespace rpc
}  // namespace gs
PROTOBUF_NAMESPACE_OPEN
template<> ::gs::rpc::QueryArgs* Arena::CreateMaybeMessage<::gs::rpc::QueryArgs>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace gs {
namespace rpc {

enum ClusterType : int {
  HOSTS = 0,
  K8S = 1,
  UNDEFINED = 100,
  ClusterType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  ClusterType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool ClusterType_IsValid(int value);
constexpr ClusterType ClusterType_MIN = HOSTS;
constexpr ClusterType ClusterType_MAX = UNDEFINED;
constexpr int ClusterType_ARRAYSIZE = ClusterType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* ClusterType_descriptor();
template<typename T>
inline const std::string& ClusterType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, ClusterType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function ClusterType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    ClusterType_descriptor(), enum_t_value);
}
inline bool ClusterType_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, ClusterType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<ClusterType>(
    ClusterType_descriptor(), name, value);
}
enum DataType : int {
  NULLVALUE = 0,
  INT8 = 1,
  INT16 = 2,
  INT32 = 3,
  INT64 = 4,
  INT128 = 5,
  UINT8 = 6,
  UINT16 = 7,
  UINT32 = 8,
  UINT64 = 9,
  UINT128 = 10,
  INT = 11,
  LONG = 12,
  LONGLONG = 13,
  UINT = 14,
  ULONG = 15,
  ULONGLONG = 16,
  FLOAT = 18,
  DOUBLE = 19,
  BOOLEAN = 20,
  STRING = 21,
  DATETIME = 22,
  LIST = 23,
  INVALID = 536870911,
  DataType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  DataType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool DataType_IsValid(int value);
constexpr DataType DataType_MIN = NULLVALUE;
constexpr DataType DataType_MAX = INVALID;
constexpr int DataType_ARRAYSIZE = DataType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* DataType_descriptor();
template<typename T>
inline const std::string& DataType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, DataType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function DataType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    DataType_descriptor(), enum_t_value);
}
inline bool DataType_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, DataType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<DataType>(
    DataType_descriptor(), name, value);
}
enum Direction : int {
  NONE = 0,
  IN = 1,
  OUT = 2,
  Direction_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  Direction_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool Direction_IsValid(int value);
constexpr Direction Direction_MIN = NONE;
constexpr Direction Direction_MAX = OUT;
constexpr int Direction_ARRAYSIZE = Direction_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* Direction_descriptor();
template<typename T>
inline const std::string& Direction_Name(T enum_t_value) {
  static_assert(::std::is_same<T, Direction>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function Direction_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    Direction_descriptor(), enum_t_value);
}
inline bool Direction_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, Direction* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<Direction>(
    Direction_descriptor(), name, value);
}
enum OutputType : int {
  GRAPH = 0,
  APP = 1,
  BOUND_APP = 2,
  RESULTS = 3,
  TENSOR = 4,
  DATAFRAME = 5,
  VINEYARD_TENSOR = 6,
  VINEYARD_DATAFRAME = 7,
  INTERACTIVE_QUERY = 8,
  GREMLIN_RESULTS = 9,
  LEARNING_GRAPH = 10,
  NULL_OUTPUT = 101,
  OutputType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  OutputType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool OutputType_IsValid(int value);
constexpr OutputType OutputType_MIN = GRAPH;
constexpr OutputType OutputType_MAX = NULL_OUTPUT;
constexpr int OutputType_ARRAYSIZE = OutputType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* OutputType_descriptor();
template<typename T>
inline const std::string& OutputType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, OutputType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function OutputType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    OutputType_descriptor(), enum_t_value);
}
inline bool OutputType_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, OutputType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<OutputType>(
    OutputType_descriptor(), name, value);
}
enum OperationType : int {
  CREATE_GRAPH = 0,
  BIND_APP = 1,
  CREATE_APP = 2,
  MODIFY_VERTICES = 3,
  MODIFY_EDGES = 4,
  RUN_APP = 5,
  UNLOAD_APP = 6,
  UNLOAD_GRAPH = 7,
  REPARTITION = 8,
  TRANSFORM_GRAPH = 9,
  REPORT_GRAPH = 10,
  PROJECT_GRAPH = 11,
  PROJECT_TO_SIMPLE = 12,
  COPY_GRAPH = 13,
  ADD_VERTICES = 14,
  ADD_EDGES = 15,
  ADD_LABELS = 16,
  TO_DIRECTED = 17,
  TO_UNDIRECTED = 18,
  CLEAR_EDGES = 19,
  CLEAR_GRAPH = 20,
  VIEW_GRAPH = 21,
  INDUCE_SUBGRAPH = 22,
  UNLOAD_CONTEXT = 23,
  SUBGRAPH = 32,
  GREMLIN_QUERY = 33,
  FETCH_GREMLIN_RESULT = 34,
  DATA_SOURCE = 46,
  DATA_SINK = 47,
  CONTEXT_TO_NUMPY = 50,
  CONTEXT_TO_DATAFRAME = 51,
  TO_VINEYARD_TENSOR = 53,
  TO_VINEYARD_DATAFRAME = 54,
  ADD_COLUMN = 55,
  GRAPH_TO_NUMPY = 56,
  GRAPH_TO_DATAFRAME = 57,
  REGISTER_GRAPH_TYPE = 58,
  GET_CONTEXT_DATA = 59,
  OUTPUT = 60,
  FROM_NUMPY = 80,
  FROM_DATAFRAME = 81,
  FROM_FILE = 82,
  GET_ENGINE_CONFIG = 90,
  OperationType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  OperationType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool OperationType_IsValid(int value);
constexpr OperationType OperationType_MIN = CREATE_GRAPH;
constexpr OperationType OperationType_MAX = GET_ENGINE_CONFIG;
constexpr int OperationType_ARRAYSIZE = OperationType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* OperationType_descriptor();
template<typename T>
inline const std::string& OperationType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, OperationType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function OperationType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    OperationType_descriptor(), enum_t_value);
}
inline bool OperationType_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, OperationType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<OperationType>(
    OperationType_descriptor(), name, value);
}
enum ParamKey : int {
  GRAPH_NAME = 0,
  DST_GRAPH_NAME = 1,
  CONTEXT_KEY = 2,
  GRAPH_TYPE = 3,
  DST_GRAPH_TYPE = 4,
  OID_TYPE = 5,
  VID_TYPE = 6,
  V_DATA_TYPE = 7,
  E_DATA_TYPE = 8,
  V_LABEL_ID = 9,
  E_LABEL_ID = 10,
  V_PROP_ID = 11,
  E_PROP_ID = 12,
  LINE_PARSER = 13,
  E_FILE = 14,
  V_FILE = 15,
  VERTEX_LABEL_NUM = 16,
  EDGE_LABEL_NUM = 17,
  DIRECTED = 18,
  V_PROP_KEY = 19,
  E_PROP_KEY = 20,
  V_DEFAULT_VAL = 21,
  E_DEFAULT_VAL = 22,
  GRAPH_TEMPLATE_CLASS = 23,
  REPARTITION_STRATEGY = 24,
  NFRAG = 25,
  PARAM = 26,
  DISTRIBUTED = 27,
  SCHEMA_PATH = 31,
  GIE_GREMLIN_QUERY_MESSAGE = 35,
  GIE_GREMLIN_REQUEST_OPTIONS = 36,
  GIE_GREMLIN_FETCH_RESULT_TYPE = 37,
  APP_SIGNATURE = 40,
  GRAPH_SIGNATURE = 41,
  IS_FROM_VINEYARD_ID = 42,
  VINEYARD_ID = 43,
  VINEYARD_NAME = 44,
  VERTEX_MAP_TYPE = 45,
  VERTEX_COLLECTIONS = 51,
  EDGE_COLLECTIONS = 52,
  GLE_HANDLE = 60,
  GLE_CONFIG = 61,
  GLE_GEN_LABELS = 62,
  APP_NAME = 100,
  APP_ALGO = 101,
  APP_LIBRARY_PATH = 102,
  OUTPUT_PREFIX = 103,
  VERTEX_RANGE = 104,
  SELECTOR = 105,
  AXIS = 106,
  GAR = 107,
  TYPE_SIGNATURE = 108,
  CMAKE_EXTRA_OPTIONS = 109,
  REPORT_TYPE = 200,
  MODIFY_TYPE = 201,
  NODE = 202,
  EDGE = 203,
  FID = 204,
  LID = 205,
  EDGE_KEY = 206,
  NODES = 207,
  EDGES = 208,
  COPY_TYPE = 209,
  VIEW_TYPE = 210,
  ARROW_PROPERTY_DEFINITION = 300,
  PROTOCOL = 301,
  VALUES = 302,
  VID = 303,
  SRC_VID = 304,
  DST_VID = 305,
  LABEL = 306,
  SRC_LABEL = 307,
  DST_LABEL = 308,
  PROPERTIES = 309,
  LOADER = 310,
  LOAD_STRATEGY = 311,
  ROW_NUM = 312,
  COLUMN_NUM = 313,
  SUB_LABEL = 315,
  GENERATE_EID = 316,
  DEFAULT_LABEL_ID = 317,
  GID = 318,
  STORAGE_OPTIONS = 321,
  READ_OPTIONS = 322,
  FD = 323,
  SOURCE = 324,
  WRITE_OPTIONS = 325,
  CHUNK_NAME = 341,
  CHUNK_TYPE = 342,
  GRAPH_LIBRARY_PATH = 400,
  VFORMAT = 500,
  EFORMAT = 501,
  JAVA_CLASS_PATH = 502,
  JVM_OPTS = 503,
  ParamKey_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  ParamKey_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool ParamKey_IsValid(int value);
constexpr ParamKey ParamKey_MIN = GRAPH_NAME;
constexpr ParamKey ParamKey_MAX = JVM_OPTS;
constexpr int ParamKey_ARRAYSIZE = ParamKey_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* ParamKey_descriptor();
template<typename T>
inline const std::string& ParamKey_Name(T enum_t_value) {
  static_assert(::std::is_same<T, ParamKey>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function ParamKey_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    ParamKey_descriptor(), enum_t_value);
}
inline bool ParamKey_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, ParamKey* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<ParamKey>(
    ParamKey_descriptor(), name, value);
}
enum ModifyType : int {
  NX_ADD_NODES = 0,
  NX_ADD_EDGES = 1,
  NX_DEL_NODES = 2,
  NX_DEL_EDGES = 3,
  NX_UPDATE_NODES = 4,
  NX_UPDATE_EDGES = 5,
  ModifyType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  ModifyType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool ModifyType_IsValid(int value);
constexpr ModifyType ModifyType_MIN = NX_ADD_NODES;
constexpr ModifyType ModifyType_MAX = NX_UPDATE_EDGES;
constexpr int ModifyType_ARRAYSIZE = ModifyType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* ModifyType_descriptor();
template<typename T>
inline const std::string& ModifyType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, ModifyType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function ModifyType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    ModifyType_descriptor(), enum_t_value);
}
inline bool ModifyType_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, ModifyType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<ModifyType>(
    ModifyType_descriptor(), name, value);
}
enum ReportType : int {
  NODE_NUM = 0,
  EDGE_NUM = 1,
  HAS_NODE = 2,
  HAS_EDGE = 3,
  NODE_DATA = 4,
  EDGE_DATA = 5,
  SUCCS_BY_NODE = 6,
  PREDS_BY_NODE = 7,
  SELFLOOPS_NUM = 8,
  NODE_ID_CACHE_BY_GID = 9,
  NODE_ATTR_CACHE_BY_GID = 10,
  SUCC_BY_GID = 11,
  PRED_BY_GID = 12,
  SUCC_ATTR_BY_GID = 13,
  PRED_ATTR_BY_GID = 14,
  SUCC_ATTR_BY_NODE = 15,
  PRED_ATTR_BY_NODE = 16,
  ReportType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::min(),
  ReportType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<int32_t>::max()
};
bool ReportType_IsValid(int value);
constexpr ReportType ReportType_MIN = NODE_NUM;
constexpr ReportType ReportType_MAX = PRED_ATTR_BY_NODE;
constexpr int ReportType_ARRAYSIZE = ReportType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* ReportType_descriptor();
template<typename T>
inline const std::string& ReportType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, ReportType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function ReportType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    ReportType_descriptor(), enum_t_value);
}
inline bool ReportType_Parse(
    ::PROTOBUF_NAMESPACE_ID::ConstStringParam name, ReportType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<ReportType>(
    ReportType_descriptor(), name, value);
}
// ===================================================================

class QueryArgs final :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:gs.rpc.QueryArgs) */ {
 public:
  inline QueryArgs() : QueryArgs(nullptr) {}
  ~QueryArgs() override;
  explicit PROTOBUF_CONSTEXPR QueryArgs(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  QueryArgs(const QueryArgs& from);
  QueryArgs(QueryArgs&& from) noexcept
    : QueryArgs() {
    *this = ::std::move(from);
  }

  inline QueryArgs& operator=(const QueryArgs& from) {
    CopyFrom(from);
    return *this;
  }
  inline QueryArgs& operator=(QueryArgs&& from) noexcept {
    if (this == &from) return *this;
    if (GetOwningArena() == from.GetOwningArena()
  #ifdef PROTOBUF_FORCE_COPY_IN_MOVE
        && GetOwningArena() != nullptr
  #endif  // !PROTOBUF_FORCE_COPY_IN_MOVE
    ) {
      InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return default_instance().GetMetadata().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return default_instance().GetMetadata().reflection;
  }
  static const QueryArgs& default_instance() {
    return *internal_default_instance();
  }
  static inline const QueryArgs* internal_default_instance() {
    return reinterpret_cast<const QueryArgs*>(
               &_QueryArgs_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(QueryArgs& a, QueryArgs& b) {
    a.Swap(&b);
  }
  inline void Swap(QueryArgs* other) {
    if (other == this) return;
  #ifdef PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() != nullptr &&
        GetOwningArena() == other->GetOwningArena()) {
   #else  // PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() == other->GetOwningArena()) {
  #endif  // !PROTOBUF_FORCE_COPY_IN_SWAP
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(QueryArgs* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  QueryArgs* New(::PROTOBUF_NAMESPACE_ID::Arena* arena = nullptr) const final {
    return CreateMaybeMessage<QueryArgs>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::Message::CopyFrom;
  void CopyFrom(const QueryArgs& from);
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  void MergeFrom( const QueryArgs& from) {
    QueryArgs::MergeImpl(*this, from);
  }
  private:
  static void MergeImpl(::PROTOBUF_NAMESPACE_ID::Message& to_msg, const ::PROTOBUF_NAMESPACE_ID::Message& from_msg);
  public:
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  uint8_t* _InternalSerialize(
      uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _impl_._cached_size_.Get(); }

  private:
  void SharedCtor(::PROTOBUF_NAMESPACE_ID::Arena* arena, bool is_message_owned);
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(QueryArgs* other);

  private:
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "gs.rpc.QueryArgs";
  }
  protected:
  explicit QueryArgs(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                       bool is_message_owned = false);
  public:

  static const ClassData _class_data_;
  const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetClassData() const final;

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kArgsFieldNumber = 1,
  };
  // repeated .google.protobuf.Any args = 1;
  int args_size() const;
  private:
  int _internal_args_size() const;
  public:
  void clear_args();
  ::PROTOBUF_NAMESPACE_ID::Any* mutable_args(int index);
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::PROTOBUF_NAMESPACE_ID::Any >*
      mutable_args();
  private:
  const ::PROTOBUF_NAMESPACE_ID::Any& _internal_args(int index) const;
  ::PROTOBUF_NAMESPACE_ID::Any* _internal_add_args();
  public:
  const ::PROTOBUF_NAMESPACE_ID::Any& args(int index) const;
  ::PROTOBUF_NAMESPACE_ID::Any* add_args();
  const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::PROTOBUF_NAMESPACE_ID::Any >&
      args() const;

  // @@protoc_insertion_point(class_scope:gs.rpc.QueryArgs)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  struct Impl_ {
    ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::PROTOBUF_NAMESPACE_ID::Any > args_;
    mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  };
  union { Impl_ _impl_; };
  friend struct ::TableStruct_graphscope_2fproto_2ftypes_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// QueryArgs

// repeated .google.protobuf.Any args = 1;
inline int QueryArgs::_internal_args_size() const {
  return _impl_.args_.size();
}
inline int QueryArgs::args_size() const {
  return _internal_args_size();
}
inline ::PROTOBUF_NAMESPACE_ID::Any* QueryArgs::mutable_args(int index) {
  // @@protoc_insertion_point(field_mutable:gs.rpc.QueryArgs.args)
  return _impl_.args_.Mutable(index);
}
inline ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::PROTOBUF_NAMESPACE_ID::Any >*
QueryArgs::mutable_args() {
  // @@protoc_insertion_point(field_mutable_list:gs.rpc.QueryArgs.args)
  return &_impl_.args_;
}
inline const ::PROTOBUF_NAMESPACE_ID::Any& QueryArgs::_internal_args(int index) const {
  return _impl_.args_.Get(index);
}
inline const ::PROTOBUF_NAMESPACE_ID::Any& QueryArgs::args(int index) const {
  // @@protoc_insertion_point(field_get:gs.rpc.QueryArgs.args)
  return _internal_args(index);
}
inline ::PROTOBUF_NAMESPACE_ID::Any* QueryArgs::_internal_add_args() {
  return _impl_.args_.Add();
}
inline ::PROTOBUF_NAMESPACE_ID::Any* QueryArgs::add_args() {
  ::PROTOBUF_NAMESPACE_ID::Any* _add = _internal_add_args();
  // @@protoc_insertion_point(field_add:gs.rpc.QueryArgs.args)
  return _add;
}
inline const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::PROTOBUF_NAMESPACE_ID::Any >&
QueryArgs::args() const {
  // @@protoc_insertion_point(field_list:gs.rpc.QueryArgs.args)
  return _impl_.args_;
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)

}  // namespace rpc
}  // namespace gs

PROTOBUF_NAMESPACE_OPEN

template <> struct is_proto_enum< ::gs::rpc::ClusterType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::ClusterType>() {
  return ::gs::rpc::ClusterType_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::DataType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::DataType>() {
  return ::gs::rpc::DataType_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::Direction> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::Direction>() {
  return ::gs::rpc::Direction_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::OutputType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::OutputType>() {
  return ::gs::rpc::OutputType_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::OperationType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::OperationType>() {
  return ::gs::rpc::OperationType_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::ParamKey> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::ParamKey>() {
  return ::gs::rpc::ParamKey_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::ModifyType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::ModifyType>() {
  return ::gs::rpc::ModifyType_descriptor();
}
template <> struct is_proto_enum< ::gs::rpc::ReportType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::gs::rpc::ReportType>() {
  return ::gs::rpc::ReportType_descriptor();
}

PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_graphscope_2fproto_2ftypes_2eproto
